class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find(low, high):
            if low > high:
                return -1

            mid = (low + high) // 2

            if target < nums[mid]:
                return find(low, mid - 1)
            if target > nums[mid]:
                return find(mid + 1, high)
            return mid

        return find(0, len(nums) - 1)