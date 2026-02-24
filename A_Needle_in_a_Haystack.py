from collections import deque, Counter

n = int(input())

for _ in range(n):
    s = input()
    t = input()
    count = Counter(t)
    for k in s:
        count[k] -= 1
    count = sorted(count.items())
    before = []
    after = []
    for k in count:
        if k[0] < s:
            for _ in range(k[1]):
                before.append(k[0])
        else:
            for _ in range(k[1]):
                after.append(k[0])
    
    # print(before, s, after)
    print(''.join(before) + s + ''.join(after)  if Counter(s) <= Counter(t) else 'Impossible')
    