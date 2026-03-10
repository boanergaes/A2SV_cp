class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        n = len(temp)
        stack = []
        res = [0]*n

        for i in range(n):
            while stack and temp[stack[-1]] < temp[i]:
                p = stack.pop()
                res[p] = i - p

            stack.append(i)

        return res