class Solution:
    def decodeString(self, s: str) -> str:
        def solve(i):
            result = []
            num = 0

            while i < len(s):
                c = s[i]

                if c.isdigit():
                    num = num * 10 + int(c)
                    i += 1

                elif c == '[':
                    inner, i = solve(i + 1)
                    result.append(inner * num)
                    num = 0

                elif c == ']':
                    return ''.join(result), i + 1

                else:  # letter
                    result.append(c)
                    i += 1

            return ''.join(result), i

        return solve(0)[0]