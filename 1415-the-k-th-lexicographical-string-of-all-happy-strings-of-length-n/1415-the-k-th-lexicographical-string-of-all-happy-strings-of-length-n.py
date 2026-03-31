class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        permutations = []
        path = []
        ref = {
            'a': ['b', 'c'],
            'b': ['a', 'c'],
            'c': ['a', 'b']
        }

        def backtrack(child):
            if len(path) == n:
                permutations.append(''.join(path))
                return
            
            for i in range(len(child)):
                path.append(child[i])
                backtrack(ref[child[i]])
                path.pop()
        
        backtrack(['a', 'b', 'c'])

        return permutations[k-1] if k <= len(permutations) else ''