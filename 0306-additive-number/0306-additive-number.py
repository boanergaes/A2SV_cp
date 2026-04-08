class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        solved = False

        def backtrack(i, curr, seq):
            nonlocal solved
            if solved:
                return True
            if len(curr) > 0 and curr[0] == '0':
                return False
            if len(seq) >= 3 and int(seq[-3]) + int(seq[-2]) != int(seq[-1]):
                return False
            if i == n:
                solved = len(seq) >= 3
                return len(seq) >= 3
            
            curr += num[i]
            seq.append(curr)
            val1 = backtrack(i+1, '', seq)
            seq.pop()

            val2 = False
            if i < n-1:
                val2 = backtrack(i+1, curr, seq)

            return val1 or val2

        return backtrack(0, '', [])
