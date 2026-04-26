class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)

        missing = n*(n+1) // 2 - sum(set(nums))
        
        freq = defaultdict(int)
        dup = 0
        for i in range(n):
            freq[nums[i]] += 1
            if freq[nums[i]] == 2:
                dup = nums[i]
                break

        return [dup, missing]