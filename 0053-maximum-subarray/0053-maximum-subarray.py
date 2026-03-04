class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        psum = [0]
        max_tot = float('-inf')

        for j in range(n):
            if psum[-1] < 0:
                psum.append(nums[j])
            else:
                psum.append(psum[-1] + nums[j])
            max_tot = max(max_tot, psum[-1])

        print(psum)

        return max_tot
