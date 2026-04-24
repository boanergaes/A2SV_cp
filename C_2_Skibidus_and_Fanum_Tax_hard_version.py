import bisect

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    
    a = [float('-inf')] + list(map(int, input().split()))
    b = sorted(map(int, input().split()))
    
    for i in range(1, n+1):
        low = bisect.bisect_left(b, a[i] + a[i-1])
        
        if a[i] >= a[i-1]:
            a[i] = min(a[i] ,b[low] - a[i]) if low < m else a[i]
        elif low < m:
            a[i] = b[low] - a[i]
        else:
            print('NO')
            break
    else:
        print('YES')