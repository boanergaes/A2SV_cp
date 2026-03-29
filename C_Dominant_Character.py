from collections import defaultdict

t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    window = defaultdict(int)
    min_len = float('inf')
    i = 0
    for j in range(n):
        window[s[j]] += 1
        
        while i < j - 1 and (window['b'] >= window['a'] or window['c'] >= window['a']):
            window[s[i]] -= 1
            i += 1
        
        if i <= j - 1:
            min_len = min(min_len, j - i + 1)
    
    print(min_len if min_len != float('inf') else -1)