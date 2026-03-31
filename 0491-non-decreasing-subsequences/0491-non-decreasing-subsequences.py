class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        subsequence = set()

        def backtrack(i, path):
            if len(path) >= 2:
                for k in range(1, len(path)):
                    if path[k] < path[k-1]:
                        break
                else:
                    subsequence.add(tuple(path))

            for j in range(i, n):
                path.append(nums[j])
                backtrack(j+1, path)
                path.pop()

        backtrack(0, [])

        return list(subsequence)