class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        path = []

        def explore(children):
            for i in range(len(children)):
                path.append(children[i])
                explore(children[:i] + children[i+1:])
                path.pop()
                
            if not children:
                permutations.append(path.copy())

        explore(nums)

        return permutations