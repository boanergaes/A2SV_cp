import sys
sys.setrecursionlimit(10**7)

def canHavePile(n, m):
    if n == m:
        return True
    if n % 3 != 0 or n == 0:
        return False
    
    next = n // 3
    return canHavePile(next, m) or canHavePile(next * 2, m)

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    print('YES' if canHavePile(n, m) else 'NO')