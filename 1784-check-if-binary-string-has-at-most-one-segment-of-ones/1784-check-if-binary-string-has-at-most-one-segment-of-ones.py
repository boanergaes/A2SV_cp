class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        zero = False
        for c in s:
            if c == '0':
                zero = True
            if zero and c == '1':
                return False
        
        return True