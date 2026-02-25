from collections import deque, Counter

n = int(input())

for _ in range(n):
    s = input()
    t = input()
    count_s = Counter(s)
    count_t = Counter(t)
    
    if not (count_s <= count_t):
        print('Impossible')
        continue

    for k in count_s:
        count_t[k] -= count_s[k]
        
    count_t = sorted(count_t.items())
    
    tt = []
    for k, v in count_t:
        for _ in range(v):
            tt.append(k)
            
    ans = []
    i = 0
    j = 0
    while i < len(s) and j < len(tt):
        if s[i] <= tt[j]:
            ans.append(s[i])
            i += 1
        else:
            ans.append(tt[j])
            j += 1
            
    ans.append(s[i:])
    ans.extend(tt[j:])
    
    print(''.join(ans))