class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = (x // 2) + 1

        while low <= high:
            mid = (low + high) // 2

            sqr = mid * mid
            if sqr > x:
                high = mid - 1
            elif sqr < x:
                low = mid + 1
            else:
                return mid
        
        return high