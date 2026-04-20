class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        tot = sum(piles)
        def valid(k):
            hours = 0
            for p in piles:
                if p % k == 0:
                    hours += p // k
                else:
                    hours += p // k + 1
            return h >= hours
        
        low = 1
        high = max(piles)

        while low <= high:
            mid = low + (high - low) // 2

            if valid(mid):
                high = mid - 1
            else:
                low = mid + 1
        
        return low