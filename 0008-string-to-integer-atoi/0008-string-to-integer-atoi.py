class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)
        stack = []
        sign = 1
        i = 0
        flag = False
        while i < n:
            if not (s[i].isnumeric() or s[i] in '+- ') or (s[i] in '+- ' and flag):
                break
            if s[i] == '-':
                sign = -1
            elif s[i].isnumeric():
                stack.append(s[i])
            if s[i] != ' ':
                flag = True
            i += 1

        n = len(stack)
        ans = 0
        house = 10 ** (n - 1)

        print(stack)
        for d in range(n):
            ans += int(stack[d]) * house
            house //= 10

        ans *= sign
        if ans > 2**31 - 1:
            return 2**31 - 1
        if ans < -2 ** 31:
            return -2 ** 31
        return ans