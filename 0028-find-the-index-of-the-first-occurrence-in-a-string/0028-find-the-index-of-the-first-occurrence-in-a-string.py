class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)

        for i in range(n):
            if haystack[i] != needle[0]:
                continue
            k = i
            j = 0
            while k < n and j < m:
                if haystack[k] != needle[j]:
                    break
                k += 1
                j += 1

            if j == m:
                return i

        return -1
