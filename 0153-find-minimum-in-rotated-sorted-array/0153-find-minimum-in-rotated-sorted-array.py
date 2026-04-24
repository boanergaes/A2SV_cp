class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            rotation = low + (high - low) // 2

            if nums[rotation] <= nums[-1]:
                high = rotation - 1
            else:
                low = rotation + 1

        return nums[low]