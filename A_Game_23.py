n, m = map(int, input().split())

count = 0

while m > n:
    if (m/2) % n == 0:
        m //= 2
        count += 1
    elif (m/3) % n == 0:
        m //= 3
        count += 1
    else:
        print(-1)
        break
else:
    print(count)
