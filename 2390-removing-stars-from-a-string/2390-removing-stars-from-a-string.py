class Solution:
    def removeStars(self, s: str) -> str:
        buff = []

        for c in s:
            if c == '*':
                buff.pop()
            else:
                buff.append(c)

        return ''.join(buff)