class Solution:
    def fib(self, n: int) -> int:
        fib_arr = [0, 1]
        for i in range(1, n+1):
            fib_arr.append(fib_arr[-1] + fib_arr[-2])
        
        return fib_arr[n]
            