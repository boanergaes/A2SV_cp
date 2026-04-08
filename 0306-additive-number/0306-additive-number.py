class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        def backtrack(i, curr, seq):
            if len(seq) > 0 and (len(seq[-1]) > 1 and seq[-1][0] == '0'):
                return False
            if len(seq) > 3 and int(seq[-4]) + int(seq[-3]) != int(seq[-2]):
                return False
            if i == n:
                return len(seq) >= 3 and int(seq[-3]) + int(seq[-2]) == int(seq[-1])
            
            curr += num[i]
            seq.append(curr)
            val1 = backtrack(i+1, '', seq)
            seq.pop()

            val2 = False
            if i < n-1:
                val2 = backtrack(i+1, curr, seq)

            return val1 or val2

        return backtrack(0, '', [])
