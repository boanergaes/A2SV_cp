class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n = len(matrix)
        m = len(matrix[0])
        self.psum = []
        for _ in range(n+1):
            self.psum.append([0] * (m+1))
        for i in range(n):
            for j in range(m):
                self.psum[i+1][j+1] = matrix[i][j] + self.psum[i+1][j] + self.psum[i][j+1] - self.psum[i][j]
        print(self.psum)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.psum[row2+1][col2+1] - self.psum[row1][col2+1] - self.psum[row2+1][col1] + self.psum[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)