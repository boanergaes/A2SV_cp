class Solution:
    def rotate(self, mat: List[List[int]]) -> None:
        # nxn mat
        n = len(mat)
        l = 0
        r = n - 1

        while l < r:
            t = l
            b = n - t - 1

            for i in range(r-l):
                temp = mat[t+i][l]
                mat[t+i][l] = mat[b][l+i]
                mat[b][l+i] = mat[b-i][r]
                mat[b-i][r] = mat[t][r-i]
                mat[t][r-i] = temp
            l += 1
            r -= 1

        return mat