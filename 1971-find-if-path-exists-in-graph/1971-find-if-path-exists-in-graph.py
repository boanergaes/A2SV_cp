class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        vis = set()
        stack = [source]

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        while stack:
            curr = stack.pop()

            if curr == destination:
                return True

            vis.add(curr)

            for nei in graph[curr]:
                if nei not in vis:
                    vis.add(nei)
                    stack.append(nei)

        return False
