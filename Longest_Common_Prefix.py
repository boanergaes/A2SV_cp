#leetcode

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        comm = list(strs[0])

        for i in range(1, len(strs)):
            j = 0
            while j < ( min( len(comm), len(strs[i]) )):
                if comm[j] != strs[i][j]:
                    comm = comm[:j]
                    break
                j += 1
            else:
                comm = comm[:j]
        
        return ''.join(comm)

        
