class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        n = len(nums)
        for i in range(n):
            for j in range(n-1):
                if int(str(nums[j]) + str(nums[j+1])) < int(str(nums[j+1]) + str(nums[j])):
                    nums[j], nums[j+1] = nums[j+1], nums[j]

        res = []
        for num in nums:
            if len(res) == 1 and res[0] == '0' and num == 0:
                continue
            res.append(str(num))

        return ''.join(res)
