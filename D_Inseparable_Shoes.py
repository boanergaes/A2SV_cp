t = int(input())

for _ in range(t):
    n = int(input())
    shoes = input().split()
    idx = {}
    for i, val in enumerate(shoes):
        if val not in idx:
            idx[val] = [i, i]
        else:
            idx[val][1] = i
            
    res = []
    for shoe in idx.values():
        if shoe[0] == shoe[1]:
            print(-1)
            break
        res.append(str(shoe[1] + 1))
        for i in range(shoe[0], shoe[1]):
            res.append(str(i+1))
    else:
        print(' '.join(res))            