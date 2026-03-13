class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if k == 0:
            for i in range(len(nums)-1):
                if nums[i] and nums[i+1]:
                    return True
            return False
        freq = {0:-1}
        total = 0
        for i , x in enumerate(nums):
            total += x
            if total%k in freq:
                if i - freq[total%k] >= 2:
                    return True
            else:
                freq[total%k] = i

        return False


        # ref = {0: -1}
        # if nums[0] % k != 0:
        #     ref[nums[0] % k] = 0

        # for i in range(1, len(nums)):
        #     nums[i] += nums[i-1]
            
        #     remainder = nums[i] % k
        #     if remainder in ref:
        #         if i - ref[remainder] > 1:
        #             return True
        #     else:
        #         ref[remainder] = i

        # return False

