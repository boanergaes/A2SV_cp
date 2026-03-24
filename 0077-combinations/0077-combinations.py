class Solution:
    def combine(self, n: int, k: int):
        combinations = []
        path = []

        def explore(c):
            if len(path) == k:
                combinations.append(path[:])
                return

            for i in range(c, n - (k - len(path)) + 2):
                path.append(i)
                explore(i + 1)
                path.pop()
                

        explore(1)

        return combinations