class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        def valid(h):
            i = 0
            while i < n and citations[i] < h:
                i += 1
            return n - i >= h

        low = 0
        high = citations[-1]

        while low <= high:
            mid = low + (high - low) // 2

            if valid(mid):
                low = mid + 1
            else:
                high = mid - 1
        
        return high











        # def valid(h):
        #     count = 0
        #     for c in citations:
        #         if c >= h:
        #             count += 1

        #     return count >= h
        
        # low = 0
        # high = citations[-1]
        # while low <= high:
        #     mid = low + (high - low) // 2

        #     if valid(mid):
        #         low = mid + 1
        #     else:
        #         high = mid - 1
        
        # return high