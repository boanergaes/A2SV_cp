class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        idx = [-1, -1]
        for i in range(len(nums)):
            if idx[0] != -1 and nums[i] == target:
                idx[1] = i
            elif nums[i] == target and idx[0] == -1:
                idx = [i, i]
            if nums[i] > target:
                return idx

        return idx