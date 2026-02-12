class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        zeros = []
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    zeros.append((i, j))
        print(zeros)
        for zero in zeros:
            for i in range(n):
                matrix[i][zero[1]] = 0
            for j in range(m):
                matrix[zero[0]][j] = 0
       