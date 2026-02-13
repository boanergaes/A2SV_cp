class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        neg = 0
        n = len(grid)
        m = len(grid[0])

        i = 0
        while i < n:
            j = 0
            while j < m:
                if grid[i][j] < 0:
                    neg += (n - i) * (m - j)
                    m = j
                    continue
                j += 1

            if j == 0:
                break
            i += 1

        return neg