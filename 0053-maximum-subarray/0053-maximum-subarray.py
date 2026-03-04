class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        max_tot = nums[0]

        for j in range(1, n):
            if nums[j-1] >= 0:
                nums[j] += nums[j-1]
            max_tot = max(max_tot, nums[j])

        return max_tot
