class Solution:
    def fib(self, n: int) -> int:
        fib_arr = [0]
        for i in range(1, n+1):
            if i == 1:
                fib_arr.append(1)
                continue
            
            fib_arr.append(fib_arr[-1] + fib_arr[-2])
        
        return fib_arr[-1]
            