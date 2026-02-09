#leetcode

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = 0
        for n in nums:
            if n%2 == 0:
                even_sum += n
                
        res = []
        
        for q in queries:
            if nums[q[1]] % 2 == 0:
                even_sum -= nums[q[1]]

            nums[q[1]] += q[0]
            if nums[q[1]] % 2 == 0:
                even_sum += nums[q[1]]

            res.append(even_sum)

        return res
        
