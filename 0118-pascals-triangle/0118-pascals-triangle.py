class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        tri = [[1]]
        for i in range(2, numRows + 1):
            toadd = [1]*i
            for j in range(1, i-1):
                toadd[j] = tri[-1][j-1] + tri[-1][j]
            tri.append(toadd)
        return tri