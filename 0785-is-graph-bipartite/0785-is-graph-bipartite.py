class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # -1: unvisited  0: black  1: white

        color_arr = [0] + [-1] * (len(graph) - 1)

        def dfs(curr):
            for nei in graph[curr]:
                if color_arr[nei] == color_arr[curr]:
                    return False
                elif color_arr[nei] == -1:
                    color_arr[nei] = 1 if color_arr[curr] == 0 else 0
                    dfs(nei)

            return True
        
        for node in range(len(graph)):
            if color_arr[node] == -1:
                color_arr[node] = 0
            if not dfs(node):
                return False

        return True