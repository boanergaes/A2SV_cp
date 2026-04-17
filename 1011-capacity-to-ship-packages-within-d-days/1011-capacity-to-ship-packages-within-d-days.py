class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        n = len(weights)
        tot = sum(weights)
        def valid(capacity):
            curr_tot = 0
            i = 0
            for _ in range(days):
                curr = 0
                while i < n and curr + weights[i] <= capacity:
                    curr += weights[i]
                    i += 1
                curr_tot += curr
            return curr_tot == tot

        low = max(weights)
        high = tot
        while low <= high:
            mid = low + (high - low) // 2
            if valid(mid):
                high = mid - 1
            else:
                low = mid + 1
        return low