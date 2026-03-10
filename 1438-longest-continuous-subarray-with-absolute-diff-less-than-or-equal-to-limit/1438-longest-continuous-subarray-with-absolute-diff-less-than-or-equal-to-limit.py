class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        minq = deque()
        maxq = deque()
        ans = 0

        i = 0
        for j in range(n):
            while minq and nums[j] < minq[-1]:
                minq.pop()
            minq.append(nums[j])
            while maxq and nums[j] > maxq[-1]:
                maxq.pop()
            maxq.append(nums[j])

            while maxq and minq and maxq[0] - minq[0] > limit:
                if nums[i] == maxq[0]:
                    maxq.popleft()
                if nums[i] == minq[0]:
                    minq.popleft()
                i += 1

            ans = max(ans, j - i + 1)

        return ans 
