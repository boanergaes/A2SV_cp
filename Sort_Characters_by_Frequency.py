#leetcode

class Solution:
    def frequencySort(self, s: str) -> str:

        f = Counter(s)
        freq = [[k, f[k]] for k in f]
        freq.sort(key=lambda k : k[1], reverse=True)
        
        ans = []
        for v in freq:
            for i in range(v[1]):
                ans.append(v[0])

        return ''.join(ans)
        
