#leetcode

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums) // 3
        nums = Counter(nums)
        res = []
        for k in nums:
            if nums[k] > n:
                res.append(k)

        return res
