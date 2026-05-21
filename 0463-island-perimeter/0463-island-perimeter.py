class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        vis = set()
        dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        perim = 0

        def inbound(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])

        def dfs(row, col):
            nonlocal perim

            vis.add((row, col))

            for dr, dc in dir:
                newr, newc = row + dr, col + dc

                if not inbound(newr, newc):
                    perim += 1
                
                elif grid[newr][newc] == 0:
                    perim += 1

                elif (newr, newc) not in vis: # and grid[newr][newc] == 1:
                    dfs(newr, newc)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in vis and grid[i][j] == 1:
                    dfs(i, j)
                    return perim