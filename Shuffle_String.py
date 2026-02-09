#leetcode

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        idx = [(val, i) for val, i in zip(s, indices)]
        out = ['']*len(s)
        for k in idx:
            out[k[1]] = k[0]

        return ''.join(out)
