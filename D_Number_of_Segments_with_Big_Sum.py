n, s = map(int, input().split())
arr = list(map(int, input().split()))

window = 0
count = 0
i = 0
for j in range(n):
    window += arr[j]
    
    while window >= s:
        count += n - j
        window -= arr[i]
        i += 1

    
print(count)
    