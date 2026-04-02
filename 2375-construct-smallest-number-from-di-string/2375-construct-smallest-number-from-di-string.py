class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        res = []
        stack = []

        for i in range(1, n+2):
            stack.append(i)

            if i == n+1 or pattern[i-1] == 'I':
                while stack:
                    res.append(str(stack.pop()))

        return ''.join(res)