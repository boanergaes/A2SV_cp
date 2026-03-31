class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        subsequence = []
        used = set()

        def backtrack(i, path):
            if len(path) >= 2:
                t = tuple(path)
                if t not in used:
                    subsequence.append(path[:])
                    used.add(t)

            while i < n and path and nums[i] < path[-1]:
                i += 1
            
            if i == n:
                return
                
            path.append(nums[i])
            backtrack(i+1, path)
            path.pop()

            backtrack(i+1, path)

        backtrack(0, [])

        return subsequence