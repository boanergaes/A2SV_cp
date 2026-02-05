class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums = Counter(nums)
        return [k for k in nums if nums[k] > 1]
