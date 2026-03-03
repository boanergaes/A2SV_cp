n, k = map(int, input().split())
arr = list(map(int, input().split()))

window = {}
good = 0
i = 0
for j in range(n):
    window[arr[j]] = window.get(arr[j], 0) + 1
    while len(window) > k:
        window[arr[i]] -= 1
        if not window[arr[i]]:
            del window[arr[i]]
        i += 1
    good += j - i + 1
    
print(good)
