class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def isSelfDiv(num):
            sn = str(num)
            for n in sn:
                if n == '0':
                    return False
                if num%int(n) != 0:
                    return False
            return True

        res = []
        for n in range(left, right + 1):
            if isSelfDiv(n):
                res.append(n)

        return res 