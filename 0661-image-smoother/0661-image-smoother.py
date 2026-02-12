class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        n = len(img)
        m =  len(img[0])

        smooth = [[0]*m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                sum = 0
                sum += img[i][j]
                tot = 1
                if i > 0:
                    sum += img[i-1][j]
                    tot += 1
                if i < n-1:
                    sum += img[i+1][j]
                    tot += 1
                if j > 0:
                    sum += img[i][j-1]
                    tot += 1
                if j < m-1:
                    sum += img[i][j+1]
                    tot += 1
                if i > 0 and j > 0:
                    sum += img[i-1][j-1]
                    tot += 1
                if i > 0 and j < m-1:
                    sum += img[i-1][j+1]
                    tot += 1
                if i < n-1 and j > 0:
                    sum += img[i+1][j-1]
                    tot += 1
                if i < n-1 and j < m-1:
                    sum += img[i+1][j+1]
                    tot += 1
                smooth[i][j] = sum//tot

        return smooth
