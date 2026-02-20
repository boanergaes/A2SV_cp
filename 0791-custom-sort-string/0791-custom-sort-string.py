class Solution:
    def customSortString(self, order: str, s: str) -> str:
        def custSrt(c):
            if c in order:
                return order.index(c)
            return 200  + ord(c)

        return ''.join(sorted(s, key=custSrt))