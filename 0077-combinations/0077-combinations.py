class Solution:
    def combine(self, n: int, k: int):
        combinations = []
        path = []

        def explore(i):
            if len(path) == k:
                combinations.append(path[:])
                return
            if i > n:
                return

            path.append(i)
            explore(i + 1)
            path.pop()

            explore(i + 1)
            

        explore(1)

        return combinations