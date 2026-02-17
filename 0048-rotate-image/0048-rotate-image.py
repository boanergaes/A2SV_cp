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
                # hold top left value
                temp = mat[t+i][l]
                # move bottom left to top left
                mat[t+i][l] = mat[b][l+i]
                # move bottom right to bottom left 
                mat[b][l+i] = mat[b-i][r]
                # move top right to bottom bottom right
                mat[b-i][r] = mat[t][r-i]
                # move the held top left to top right
                mat[t][r-i] = temp
            l += 1
            r -= 1

        return mat