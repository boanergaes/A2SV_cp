class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        psum = [0]
        ref = {0: 0}
        for i in range(n):
            psum.append(psum[-1] + nums[i])
            remainder = psum[i+1] % k
            if remainder in ref:
                if i > ref[remainder]:
                    return True
            else:
                ref[remainder] = i + 1

        return False