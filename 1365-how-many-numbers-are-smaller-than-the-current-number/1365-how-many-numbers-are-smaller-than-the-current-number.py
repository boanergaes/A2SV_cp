class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        srtd = sorted(nums)
        idx = {}
        for i, num in enumerate(srtd):
            if num not in idx:
                idx[num] = i
        
        return [idx[n] for n in nums]