t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    k = 0
    opp = []
    for i in range(n):
        for j in range(n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                k += 1
                opp.append(f"1 {j+1}")
            if b[j] > b[j+1]:
                b[j], b[j+1] = b[j+1], b[j]
                k += 1
                opp.append(f"2 {j+1}")
    
    for i in range(n):
        if a[i] > b[i]:
            k += 1
            opp.append(f"3 {i+1}")

    print(k)
    for o in opp:
        print(o)