class Solution:
    def splitString(self, s: str) -> bool:
        n = len(s)

        def backtrack(i, curr, seq):
            if len(seq) >= 2 and seq[-2] - seq[-1] != 1:
                return False
            if i == n:
                return len(seq) >= 2

            curr = curr * 10 + int(s[i])
            seq.append(curr)
            val1 = backtrack(i+1, 0, seq)
            seq.pop()

            val2 = False
            if i < n - 1:
                val2 = backtrack(i+1, curr, seq)

            return val1 or val2

        return backtrack(0, 0, [])