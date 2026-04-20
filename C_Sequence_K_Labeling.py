from collections import defaultdict

n, k = map(int, input().split())
seq = list(map(int, input().split()))

label_map = defaultdict(set)
labels = []
l = 1

def solve():
    global l
    flag = True
    for num in seq:
        found = False
        if l in label_map[num]:
            for i in range(1, k+1):
                if i not in label_map[num]:
                    labels.append(i)
                    label_map[num].add(i)
                    # found = True
                    break
            else:
                return 'NO'
            continue
        
        labels.append(l)
        label_map[num].add(l)
        found = True
        l += 1
        if l == k + 1:
            l = 1
    
    return 'YES'

res = solve()

if res == 'NO':
    print('NO')
else:
    print('YES')
    for i in labels:
        print(i, end=' ')
    print()