from collections import Counter

n, m = list(map(int, input().split()))
a = Counter(map(int, input().split()))
b = Counter(map(int, input().split()))

tot = 0
for k in a:
    if k in b:
        tot += a[k] * b[k]
        
print(tot)