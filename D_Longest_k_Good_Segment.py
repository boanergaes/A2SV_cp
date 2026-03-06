from collections import defaultdict

n, k = map(int, input().split())
arr = list(map(int, input().split()))
window = defaultdict(int)
span = ()
max_len = 0

i = 0
for j in range(n):
    window[arr[j]] += 1
    
    while len(window) > k:
        window[arr[i]] -= 1
        if not window[arr[i]]:
            del window[arr[i]]
        i += 1
        
    if j - i + 1 > max_len:
        max_len = j - i + 1
        span = (i, j)
        
print(span[0] + 1, span[1] + 1)