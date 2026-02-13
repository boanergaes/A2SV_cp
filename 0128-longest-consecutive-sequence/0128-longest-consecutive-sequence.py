class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_len = 0

        for n in nums:
            if n-1 not in nums:
                curr = 1
                while n + 1 in nums:
                    curr += 1
                    n += 1

                max_len = max(curr, max_len)

        return max_len