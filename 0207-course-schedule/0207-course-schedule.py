class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # -1: gray(unvisited)  0: white(expanded)  1: black(finished)
        GRAY, WHITE, BLACK = -1, 0, 1
        color = [GRAY] * numCourses
        graph = defaultdict(list)

        for i, j in prerequisites:
            graph[i].append(j)

        def iscycle(node):
            if color[node] == WHITE:
                return False

            color[node] = WHITE

            for nei in graph[node]:
                if color[nei] != BLACK:
                    if not iscycle(nei):
                        return False

            color[node] = BLACK
            return True


        for node in range(numCourses):
            if color[node] != BLACK and not iscycle(node):
                return False

        return True