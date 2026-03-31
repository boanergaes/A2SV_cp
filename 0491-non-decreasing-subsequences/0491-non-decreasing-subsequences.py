class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        subsequence = []

        def backtrack(i, path):
            if len(path) >= 2:
                subsequence.append(path[:])

            vis = set()
            for j in range(i, n):
                if (path and nums[j] < path[-1]) or nums[j] in vis:
                    continue
                vis.add(nums[j])
                path.append(nums[j])
                backtrack(j+1, path)
                path.pop()

        backtrack(0, [])

        return subsequence