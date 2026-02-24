class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        sc = int(sqrt(c)) + 1
        for i in range(sc):
            print(i ** 2, c - i ** 2)
            if int(sqrt(c - i ** 2)) ** 2 == c - i ** 2:
                return True
        return False