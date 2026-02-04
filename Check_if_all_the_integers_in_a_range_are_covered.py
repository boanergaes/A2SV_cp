#leetcode

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        target = [i for i in range(left, right+1)]

        for r in ranges:
            for j in range(r[0], r[1]+1):
                if j in target:
                    target.remove(j)

        return not target
