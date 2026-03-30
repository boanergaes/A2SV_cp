class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        path = []

        def permute(child):
            if not child:
                permutations.append(path[:])
                return

            for i in range(len(child)):
                path.append(child[i])
                permute(child[:i] + child[i+1:])
                path.pop()

            
        permute(nums)

        return permutations