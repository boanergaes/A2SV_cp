t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    casinos = []
    for _ in range(n):
        casinos.append(list(map(int, input().split())))
    
    casinos.sort(key=lambda x : x[0])
    for casino in casinos:
        if casino[0] <= k <= casino[1]:
            k = max(k, casino[2])
        else:
            continue
    print(k)