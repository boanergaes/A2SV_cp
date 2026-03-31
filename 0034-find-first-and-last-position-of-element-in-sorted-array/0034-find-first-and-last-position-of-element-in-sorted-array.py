class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if  target < nums[mid]:
                high = mid - 1
            elif target > nums[mid]:
                low = mid + 1
            else:
                while nums[low] != target:
                    low += 1
                while nums[high] != target:
                    high -= 1
                return [low, high]

        return [-1, -1]