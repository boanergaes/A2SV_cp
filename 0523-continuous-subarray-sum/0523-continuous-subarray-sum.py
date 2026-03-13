class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        ref = {0: -1}
        if nums[0] % k != 0:
            ref[nums[0] % k] = 0

        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
            
            remainder = nums[i] % k
            if remainder in ref:
                if i - ref[remainder] > 1:
                    return True
            else:
                ref[remainder] = i

        return False