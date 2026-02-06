#leetcode

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_f = {}
        map_b = {}

        for c, d in zip(s, t):
            if c in map_f and map_f[c] != d:
                return False
            if d in map_b and map_b[d] != c:
                return False
            map_f[c] = d
            map_b[d] = c
        
        return True
