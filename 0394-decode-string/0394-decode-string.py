class Solution:
    def decodeString(self, s: str) -> str:
        def solve(k, rem):
            cbn = []
            num = 0
            i = 0
            while i < len(rem):
                c = rem[i]
                if c.isnumeric():
                    narr = []
                    while rem[i].isnumeric():
                        narr.append(rem[i])
                        i += 1
                    num = int(''.join(narr))
                elif c.isalpha():
                    cbn.append(c)
                    i += 1
                elif c == '[':
                    incoming, curri = solve(num, rem[i+1:])
                    cbn += incoming
                    i += curri + 2
                elif c == ']':
                    final = []
                    for _ in range(k):
                        final.extend(cbn)
                    return [final, i]

        num = 0
        decoded = []
        char_buff = []
        i = 0
        while i < len(s):
            c = s[i]
            if c.isnumeric():
                narr = []
                while s[i].isnumeric():
                    narr.append(s[i])
                    i += 1
                num = int(''.join(narr))
                decoded.extend(char_buff)
                char_buff = []
            elif c == '[':
                incoming, curri = solve(num, s[i+1:])
                decoded += incoming
                decoded.extend(char_buff)
                char_buff = []
                i += curri + 2
            elif c.isalpha():
                char_buff.append(c)
                i += 1
        
        decoded.extend(char_buff)
        return ''.join(decoded)