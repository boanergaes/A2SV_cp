n, s = map(int, input().split())
arr = list(map(int, input().split()))

window = 0
count = 0
i = 0
for j in range(n):
    window += arr[j]
    
    while window > s:
        window -= arr[i]
        i += 1
    
    count += j - i + 1
    
print(count)
    