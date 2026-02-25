class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {k: i for i, k in enumerate(s)}
        
        max_last = 0
        last_valid = 0
        ans = []
        for i, k in enumerate(s):
            max_last = max(max_last, last_index[k])
            if i == max_last:
                ans.append(i - last_valid + 1)
                last_valid = i + 1
        
        return ans