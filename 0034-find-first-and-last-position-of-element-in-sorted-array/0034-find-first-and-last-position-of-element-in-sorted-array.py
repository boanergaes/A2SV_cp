class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = bisect_left(nums, target)
        right =  bisect_right(nums, target)

        print(left, right)
        if left < 0 or left >= len(nums) or right - 1 < 0 or right - 1 >= len(nums):
            return [-1, -1]

        return [left if nums[left] == target else -1, right - 1 if nums[right - 1] == target else -1]