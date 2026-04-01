class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        count = 0
        ans = ''
        path = []
        ref = {
            'a': ['b', 'c'],
            'b': ['a', 'c'],
            'c': ['a', 'b']
        }

        def backtrack(child):
            nonlocal count
            nonlocal ans

            if count >= k:
                return

            if len(path) == n:
                count += 1
                if count == k:
                    ans = ''.join(path)
                return
            
            for i in range(len(child)):
                path.append(child[i])
                backtrack(ref[child[i]])
                path.pop()
        
        backtrack(['a', 'b', 'c'])

        return ans