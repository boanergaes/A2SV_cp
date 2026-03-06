from collections import Counter

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = input()
    window = Counter(s[:k])
    ans = k - window.get('B', 0)

    i = 0
    for j in range(k, n):
        window[s[j]] = window.get(s[j], 0) + 1
        window[s[i]] -= 1
        i += 1
        ans = min(ans, k - window.get('B', 0))
        
    print(ans)