#leetcode

class Solution:
    def intToRoman(self, num: int) -> str:
        toRoman = {
            1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M'
        }

        sn = str(num)
        l = len(sn)
        res = []

        for i in range(l):
            house = 10**(l - i - 1)
            cnum = int(sn[i]) * house

            if sn[i] == '4' or sn[i] == '9':
                res.append(toRoman[house] + toRoman[cnum + house])

            elif sn[i] != '5':
                t = int(sn[i])
                if t <= 3:
                    res.append(toRoman[house] * t)
                    continue

                res.append(toRoman[5*house] + toRoman[house] * (t - 5))

            else:
                res.append(toRoman[cnum])

        print(res)
        return ''.join(res)

            

            
