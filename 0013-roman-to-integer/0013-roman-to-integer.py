class Solution:
    def romanToInt(self, s: str) -> int:
        toInt = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        num = 0
        i = 0
        while i < len(s):
            if i < len(s) - 1 and toInt[s[i]] < toInt[s[i+1]]:
                num += toInt[s[i+1]] - toInt[s[i]]
                i += 2
            else:
                num += toInt[s[i]]
                i += 1

        return num
            