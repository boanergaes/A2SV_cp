class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        powerSet = []
        path = []

        def backtrack(i):
            powerSet.append(path[:])
            
            seen  = set()
            for j in range(i, n):
                if nums[j] in seen:
                    continue
                seen.add(nums[j])
                path.append(nums[j])
                backtrack(j+1)
                path.pop()

        backtrack(0)

        return list(powerSet)