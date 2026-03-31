class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        powerSet = []
        path = []

        def backtrack(i):
            powerSet.append(path[:])
            
            for j in range(i, n):
                if j > i and nums[j] == nums[j-1]:
                    continue
                    
                path.append(nums[j])
                backtrack(j+1)
                path.pop()

        backtrack(0)

        return list(powerSet)