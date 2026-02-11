class Solution:
    def frequencySort(self, s: str) -> str:
        count = list(Counter(s).items())
        count.sort(key=lambda x : x[1], reverse=True)
        ans = []
        for ch in count:
            for _ in range(ch[1]):
                ans.append(ch[0])

        return ''.join(ans)
