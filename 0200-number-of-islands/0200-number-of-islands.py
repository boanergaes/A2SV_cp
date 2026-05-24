class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        vis = set()

        def isbound(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])

        def dfs(row, col):
            nonlocal vis

            for r, c in dir:
                newr = row + r
                newc = col + c

                if (newr, newc) not in vis and isbound(newr, newc) and grid[newr][newc] == '1':
                    vis.add((newr, newc))
                    dfs(newr, newc)

        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and (i, j) not in vis:
                    dfs(i, j)
                    islands += 1

        return islands
