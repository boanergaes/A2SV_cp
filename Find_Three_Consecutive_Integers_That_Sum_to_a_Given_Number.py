#leetcode

class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        r = num//3
        return [r-1, r, r+1] if r*3 == num else []
