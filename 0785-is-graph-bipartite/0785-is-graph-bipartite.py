class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        clrarr = [-1] * len(graph)

        def dfs(curr):
            if clrarr[curr] == -1:            
                clrarr[curr] = 0

            for nei in graph[curr]:
                if clrarr[nei] == clrarr[curr]:
                    return False
                elif clrarr[nei] == -1:
                    clrarr[nei] = 1 if clrarr[curr] == 0 else 0
                    dfs(nei)

            return True
        
        for node in range(len(graph)):
            if not dfs(node):
                return False

        return True