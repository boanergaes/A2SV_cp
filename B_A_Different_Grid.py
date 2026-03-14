t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    
    if n == m and n == 1:
        input()
        print(-1)
    
    elif m == 1:
        cols = []
        for _ in range(n):
            cols.append(input())
        i = 0
        j = n - 1
        while i < j:
            cols[i], cols[j] = cols[j], cols[i]
            i += 1
            j -= 1
        cols[0], cols[j] = cols[j], cols[0]
        for c in cols:
            print(c)
    else:
        for _ in range(n):
            row = input().split()
            i, j = 0, m - 1
            while i < j:
                row[i], row[j] = row[j], row[i]
                i += 1
                j -= 1
            row[0], row[j] = row[j], row[0]
            print(' '.join(row))