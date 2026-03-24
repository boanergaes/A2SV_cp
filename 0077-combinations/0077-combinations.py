class Solution:
    def combine(self, n: int, k: int):
        nums = [i + 1 for i in range(n)]
        combinations = set()
        path = set()

        def explore(children):
            if len(path) == k:
                combinations.add(tuple(path.copy()))
                return
            if not children:
                if len(path) == k:
                    combinations.add(tuple(path.copy()))
                return

            for i in range(len(children)):
                path.add(children[i])
                explore(children[i+1:])
                path.remove(children[i])
                

        explore(nums)

        return [list(combination) for combination in combinations]