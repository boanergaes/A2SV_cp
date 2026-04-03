class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        res = []
        buff = []

        for i in range(1, n + 2):
            buff.append(str(i))

            if i == n + 1 or pattern[i-1] == 'I':
                res.extend(buff[::-1])
                buff = []

        return ''.join(res)