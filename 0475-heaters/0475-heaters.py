class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        rad = 0

        for house in houses:
            min_dist = float('inf')
            low = 0
            high = len(heaters) - 1

            while low <= high:
                mid = low + (high - low) // 2

                min_dist = min(min_dist, abs(house - heaters[mid]))

                if heaters[mid] > house:
                    high = mid - 1
                else:
                    low = mid + 1
            
            rad = max(rad, min_dist)

        return rad