class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1:
            return s
        srtd = sorted(s[:n//2])
        if n%2 != 0:
            srtd.append(s[n//2])
        srtd.extend(srtd[n//2 - 1::-1])
        return ''.join(srtd)