class Solution:
    def decodeString(self, s: str) -> str:
        def solve(i):
            res = []
            num = 0

            while i < len(s):
                c = s[i]

                if c.isnumeric():
                    num = num * 10 + int(c)
                    i += 1
                
                elif c == '[':
                    inner, i = solve(i+1)
                    res.append(inner * num)
                    num = 0
                
                elif c == ']':
                    return ''.join(res), i+1
                else:
                    res.append(c)
                    i += 1
                    
            return ''.join(res), i

        return solve(0)[0]