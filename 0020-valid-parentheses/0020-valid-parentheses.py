class Solution:
    def isValid(self, s: str) -> bool:
        ref = {
            '}': '{',
            ']': '[',
            ')': '('
        }
        stack = []
        
        for c in s:
            if c in '{([':
                stack.append(c)
            elif stack and ref[c] == stack[-1]:
                stack.pop()
            else:
                return False
        
        return not stack