class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # -1: gray(unvisited)  0: white(expanded)  1: black(finished)
        color = [-1] * numCourses
        graph = defaultdict(list)

        for i, j in prerequisites:
            graph[i].append(j)

        def iscycle(node):
            if color[node] == 0:
                return False

            color[node] = 0

            for nei in graph[node]:
                if color[nei] != 1:
                    if not iscycle(nei):
                        return False

            color[node] = 1
            return True


        for node in range(numCourses):
            if color[node] != 1 and not iscycle(node):
                return False

        return True