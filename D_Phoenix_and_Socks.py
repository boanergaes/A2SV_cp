# ========== I DON'T UNDERSTAND!!! ================

from collections import Counter

t = int(input())

for _ in range(t):
    n, l, r = map(int, input().split())
    socks = list(map(int, input().split()))
    left = socks[:n//2]
    right = Counter(socks[n//2:])
    costs = abs(n//2 - l)

    for num in left:
        if num not in right or right[num] == 0:
            costs += 1
            continue

        right[num] -= 1
        
    print(costs)
