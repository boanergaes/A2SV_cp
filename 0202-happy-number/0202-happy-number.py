class Solution:
    def isHappy(self, n: int) -> bool:
        while n//10 != 0:
            total = 0
            while n:
                total += (n%10) ** 2
                n //= 10
            n = total

        # 1 and 7 are the only one digit happy numbers
        return n == 1 or n == 7