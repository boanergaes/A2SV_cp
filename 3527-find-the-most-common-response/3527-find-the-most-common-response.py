class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        count = {}
        for res in responses:
            unique = set(res)
            for r in unique:
                count[r] = count.get(r, 0) + 1

        most_common = ''
        max_freq = 0
        for k, val in count.items():
            if val == max_freq:
                most_common = min(most_common, k)
            elif val > max_freq:
                max_freq = val
                most_common = k

        return most_common