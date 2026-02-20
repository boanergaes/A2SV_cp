class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        count = Counter(nums)
        return [k for k in count if count[k]  > n//3]