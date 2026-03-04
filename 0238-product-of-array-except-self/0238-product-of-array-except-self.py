class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_sum = [1]
        suffix_sum = [1]*n

        for i in range(1, n):
            prefix_sum.append(prefix_sum[-1] * nums[i-1])
            si = n - i - 1
            suffix_sum[si] = suffix_sum[si+1] * nums[si+1]
        
        return [prefix_sum[i] * suffix_sum[i] for i in range(n)]