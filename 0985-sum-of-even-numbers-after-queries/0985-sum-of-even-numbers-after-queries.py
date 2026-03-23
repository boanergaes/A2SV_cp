class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = 0
        for n in nums:
            if n % 2 == 0:
                even_sum += n

        track = []
        for q in queries:
            val = q[0]
            i = q[1]
            if nums[i] % 2 == 0:
                even_sum -= nums[i]
            nums[i] += val
            if nums[i] % 2 == 0:
                even_sum += nums[i]
            track.append(even_sum)

        return track