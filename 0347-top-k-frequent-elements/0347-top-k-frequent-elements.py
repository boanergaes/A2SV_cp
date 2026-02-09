class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = list(Counter(nums).items())
        count = sorted(count, reverse=True, key=lambda x : x[1])

        return [count[i][0] for i in range(k)]