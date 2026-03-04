class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        n = len(nums)
        start_val = 1
        psum = [0]
        for i in range(n):
            psum.append(psum[-1] + nums[i])
            if psum[-1] < 0:
                start_val = max(start_val, abs(psum[-1]) + 1)

        return start_val