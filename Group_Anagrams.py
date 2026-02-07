#leetcode

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counts = {}
        for s in strs:
            count =  frozenset(Counter(s).items())
            if count in counts:
                counts[count].append(s)
            else:
                counts[count] = [s]

        return list(counts.values())
