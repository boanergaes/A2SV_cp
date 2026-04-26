class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def valid(dist):
            curr = 0
            count = 1
            for i in range(1, len(position)):
                if position[i] - position[curr] >= dist:
                    curr = i
                    count += 1
            
            return count >= m

        low = 1
        high = position[-1] - position[0]

        while low <= high:
            mid = (low + high) // 2

            if valid(mid):
                low = mid + 1
            else:
                high = mid - 1

        return high 