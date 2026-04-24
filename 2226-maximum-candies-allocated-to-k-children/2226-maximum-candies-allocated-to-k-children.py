class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def valid(cand):
            if cand == 0:
                return True
                
            child = 0

            for c in candies:
                child += c // cand
            
            return child >= k

        low = 0
        high = max(candies)

        while low <= high:
            mid = low + (high - low) // 2

            if valid(mid):
                low = mid + 1
            else:
                high = mid - 1

        return high