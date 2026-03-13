class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        ref = {0: -1}
        running = 0
        for i in range(len(nums)):
            running += nums[i]
            remainder = running % k
            if remainder in ref:
                if i - ref[remainder] > 1:
                    return True
            else:
                ref[remainder] = i

        return False

