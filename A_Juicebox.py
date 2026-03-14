from collections import defaultdict
from random import randint

rand = randint(1000, 10**6)

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    pairs = {}
    for _ in range(k):
        b, c = map(int, input().split())
        pairs[b ^ rand] = pairs.get(b ^ rand, 0) + c
    
    pairs = sorted(pairs.values(), reverse=True)
    profit = 0
    for pair in pairs:
        if n == 0:
            break
        profit += pair
        n -= 1
        
    print(profit)