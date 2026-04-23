class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        # for i in range(numCourses):
        #     graph[i] = -1
        for v in prerequisites:
            graph[v[0]].append(v[1])

        w = 1
        g = 2
        b = 3
        cycle = False
        color = [w]*numCourses

        def dfs(node):
            nonlocal cycle
            if cycle:
                return

            if node in graph:
                color[node] = g
                for nei in graph[node]:
                    if color[nei] == w:
                        dfs(nei)
                    elif color[nei] == g:
                        cycle = True
                    
                color[node] = b

        for node in graph:
            if color[node] == w:
                dfs(node)
            
        return not cycle