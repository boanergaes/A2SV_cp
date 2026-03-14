class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x : x[1])
        last_arrow_pos = float('-inf')
        arrow_count = 0

        for pt in points:
            if pt[0] > last_arrow_pos:
                last_arrow_pos = pt[1]
                arrow_count += 1
        
        return arrow_count