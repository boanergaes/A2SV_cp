class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def dec_wind(wind, key):
            wind[key] -= 1
            if not wind[key]:
                del wind[key]

        n = len(nums)
        window = {}
        good = 0

        far_left = 0
        near_left = 0
        for right in range(n):
            window[nums[right]] = window.get(nums[right], 0) + 1

            while len(window) > k:
                dec_wind(window, nums[near_left])
                near_left += 1
                far_left = near_left
            
            while (window[nums[near_left]] > 1 and window[nums[right]] > 1) or window[nums[near_left]] > 1:
                dec_wind(window, nums[near_left])
                near_left += 1
            
            if len(window) == k:
                good += near_left - far_left + 1

        return good