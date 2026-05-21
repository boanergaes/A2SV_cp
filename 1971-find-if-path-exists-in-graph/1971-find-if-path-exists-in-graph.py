class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        vis = set()

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def hasValidPath(curr):
            if curr == destination:
                return True

            for nei in graph[curr]:
                if nei not in vis:
                    vis.add(nei)
                    if hasValidPath(nei):
                        return True

            return False

        return hasValidPath(source)