class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        psum = [0]
        for i in range(n):
            psum.append(psum[-1] + nums[i])

        ref = {0: 0}
        for i in range(1, n+1):
            remainder = psum[i] % k
            if remainder in ref:
                if i - ref[remainder] > 1:
                    return True
            else:
                ref[remainder] = i

        return False