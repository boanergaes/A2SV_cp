class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        score = 0

        for i in range(len(s)):
            b = s[i]
            if b == '(':
                stack.append(b)
            else:
                if s[i-1] == '(':
                    score += 2**(len(stack) - 1)
                stack.pop()

        return score