#codeforces

from collections import Counter

# check if the orders of chars in s and t are the same, if not, print NO
# if the orders are the same, count the number of chars needed to transform s to t
# and count the number of chars available in p, if the needed chars are more than the available chars, print NO, otherwise print YES

n = int(input())

for _ in range(n):
    s = input()
    t = input()
    p = input()
    
    need = {}
    
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
            j += 1
        else:
            need[t[j]] = need.get(t[j], 0) + 1
            j += 1
    while j < len(t):
        need[t[j]] = need.get(t[j], 0) + 1
        j += 1
    d
    have = Counter(p)
    
    for k in need:
        if have[k] < need[k]:
            print('NO')
            break
    else:
        print('YES')
    