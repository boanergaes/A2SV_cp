#leetcode 

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        idx1 = {val: i for i, val in enumerate(list1)}
        idx2 = {val: i for i, val in enumerate(list2)}

        res = []
        mi = float('inf')

        for k in idx1:
            if k in idx2:
                if idx1[k] + idx2[k] < mi:
                    mi = idx1[k] + idx2[k]
                    res = [k]
                elif idx1[k] + idx2[k] == mi:
                    res.append(k)

        return res
