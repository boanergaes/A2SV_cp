t = int(input())

for _ in range(t):
    n = int(input())
    togos = []
    for _ in range(n):
        togos.append(list(map(int, input().split())))
    togos.sort(key=lambda x : x[1])
    print(togos)
    srtd_idx = {val[0]: i for val, i in enumerate(sorted(togos, key=lambda x : x[0]))}
    print(srtd_idx)
    
    greetings = 0
    for i in range(n - 1):
        for j in range(i+1, n):
            if togos[j][0] < togos[i][0]:
                greetings += 1
                
    print(greetings)