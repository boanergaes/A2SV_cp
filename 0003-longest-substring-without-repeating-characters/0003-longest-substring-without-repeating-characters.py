class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        count = {}
        long = 0

        i = 0
        for j in range(n):
            count[s[j]] = count.get(s[j], 0) + 1
            while i < j and count[s[j]] > 1:
                count[s[i]] -= 1
                i += 1
            long = max(long, j - i + 1)

        return long