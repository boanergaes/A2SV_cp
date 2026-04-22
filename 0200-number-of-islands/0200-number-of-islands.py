class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def inbound(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])

        dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        vis = set()
        islands = 0

        def dfs(row, col):
            vis.add((row, col))

            for x, y in dir:
                newr, newc = row + x, col + y

                if inbound(newr, newc) and grid[row][col] == '1' and (newr, newc) not in vis:
                    dfs(newr, newc)   

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and (i, j) not in vis:
                    islands += 1
                    dfs(i, j)

        return islands             