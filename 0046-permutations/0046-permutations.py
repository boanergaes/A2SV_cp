class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        path = []

        def explore(children):
            for i in range(len(children)):
                path.append(children[i])
                explore(children[:i] + children[i+1:])
                path.remove(children[i])
                
            if not children:
                permutations.append(deepcopy(path))

        explore(nums)

        return permutations