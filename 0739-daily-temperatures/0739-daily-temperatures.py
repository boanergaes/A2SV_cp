class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        n = len(temp)
        q = deque()
        arr = [0]*n
        for i in range(n):
            while q and temp[i] > temp[q[-1]]:
                arr[q[-1]] = i - q[-1]
                q.pop()
            q.append(i)
        return arr