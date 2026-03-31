class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        powerSet = []
        path = []

        def backtrack(i):
            
            if i == n:
                powerSet.append(path[:])
                return

            path.append(nums[i])
            backtrack(i+1)
            path.pop()

            while i < n-1 and nums[i] == nums[i+1]:
                i += 1

            backtrack(i+1)

        backtrack(0)

        return list(powerSet)