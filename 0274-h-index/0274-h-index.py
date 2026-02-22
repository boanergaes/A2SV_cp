class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        h = 0
        while h < len(citations):
            if citations[h] >= h+1:
                h += 1
            else:
                break

        return h