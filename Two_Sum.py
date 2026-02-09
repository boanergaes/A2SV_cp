#leetcode

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        ref = {}
        for i in range(n):
            if nums[i] in ref:
                return [ref[nums[i]], i]
            ref[target - nums[i]] = i
