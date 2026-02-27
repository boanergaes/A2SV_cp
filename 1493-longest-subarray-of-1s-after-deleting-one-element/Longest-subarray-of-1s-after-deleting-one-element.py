class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        window = {0: 0, 1: 0}
        max_freq = 0
        ans = 0
        i = 0
        for j in range(len(nums)):
            window[nums[j]] += 1
            max_freq = max(max_freq, window[1])

            while j - i + 1 - max_freq > 1:
                window[nums[i]] -= 1
                i += 1
            
            ans = max(ans, j - i)

        return ans
