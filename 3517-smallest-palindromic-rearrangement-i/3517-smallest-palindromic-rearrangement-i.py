class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        s_count = sorted(s)
        s_count = Counter(s_count)
        answer = [""] * n
        start, end = 0, n - 1

        for key, val in s_count.items():
            pairs = val // 2
            for _ in range(pairs):
                answer[start] = key
                answer[end] = key
                start += 1
                end -= 1

        mid_char = s[n // 2]

        if n%2 != 0:
            answer[len(s)//2] = mid_char

        return "".join(answer)