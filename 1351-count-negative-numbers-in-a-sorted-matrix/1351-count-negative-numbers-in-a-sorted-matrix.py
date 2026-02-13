class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        neg = 0
        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            for j in range(m):
                if grid[i][j] < 0:
                    neg += 1

        return neg