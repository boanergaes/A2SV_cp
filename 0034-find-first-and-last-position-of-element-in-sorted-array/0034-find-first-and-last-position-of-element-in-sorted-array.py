class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_lower():
            left = 0
            right = len(nums) - 1

            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1

            return left if left < len(nums) and nums[left] == target else -1
        
        def find_upper():
            left = 0
            right = len(nums) - 1

            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1

            return right if right >= 0 and nums[right] == target else -1
        
        return [ find_lower(), find_upper()]