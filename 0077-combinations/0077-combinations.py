class Solution:
    def combine(self, n: int, k: int):
        nums = [i + 1 for i in range(n)]
        combinations = []
        path = []

        def explore(children):
            if len(path) == k:
                combinations.append(tuple(path.copy()))
                return
            if not children:
                if len(path) == k:
                    combinations.append(tuple(path.copy()))
                return

            for i in range(len(children)):
                path.append(children[i])
                explore(children[i+1:])
                path.pop()
                

        explore(nums)

        return [list(combination) for combination in combinations]