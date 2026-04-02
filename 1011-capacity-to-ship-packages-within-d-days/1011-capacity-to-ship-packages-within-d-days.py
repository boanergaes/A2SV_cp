class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        tot_weight = sum(weights)
        def valid(cap):
            curr = 0
            tot = 0
            i = 0
            for _ in range(days):
                while i < len(weights) and curr + weights[i] <= cap:
                    curr += weights[i]
                    i += 1 
                tot += curr
                curr = 0

            return tot == tot_weight

        low = max(weights)
        high = tot_weight

        while low <= high:
            mid = low + (high - low) // 2

            if valid(mid):
                high = mid - 1
            else:
                low = mid + 1

        return low