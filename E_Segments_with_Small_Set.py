n, k = map(int, input().split())
arr = list(map(int, input().split()))

window = {}
count = 0
once = 0
i = 0
for j in range(n):
    window[arr[j]] = window.get(arr[j], 0) + 1
    
    if window[arr[j]] == 1:
        once += 1
    else:
        once -= 1
    
    while i < j and once > k:
        if window[arr[i]] == 1:
            once -= 1
        window[arr[i]] -= 1
        if window[arr[i]] == 1:
            once += 1
        i += 1
        
    count += j
    
print(count)