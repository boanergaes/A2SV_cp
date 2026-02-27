class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        window = {}
        max_freq = 0
        ans = 0
        i = 0
        for j in range(n):
            window[s[j]] = window.get(s[j], 0) + 1
            max_freq = max(max_freq, window[s[j]])

            while j - i + 1 - max_freq > k:
                window[s[i]] -= 1
                i += 1

            ans = max(ans, j - i + 1)

        return ans