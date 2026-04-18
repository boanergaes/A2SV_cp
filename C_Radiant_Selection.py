import math

t = int(input())

def possible(n, k):
    return n - math.isqrt(n) >= k

for _ in range(t):
    k = int(input())
    
    low = 1
    high = 2 * 10**18
    ans = -1
    
    while low <= high:
        mid = low + (high - low) // 2
        
        if possible(mid, k):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
            
    print(ans)