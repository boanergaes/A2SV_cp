class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        n = len(img)
        m =  len(img[0])

        smooth = [[0]*m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                total = 0
                count = 0
                
                for r in range(max(i-1, 0), min(i+2, n)):
                    for c in range(max(j-1, 0), min(j+2, m)):
                        total += img[r][c]
                        count += 1
                smooth[i][j] = total // count                

        return smooth
