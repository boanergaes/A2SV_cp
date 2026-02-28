t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    arr = sorted(map(int, input().split()))
    count = 0
    unique = {}
    i = 0
    for j in range(n):
        if j > 0 and arr[j] > arr[j-1] + 1:
            i = j
            unique.clear()

        unique[arr[j]] = unique.get(arr[j], 0) + 1
        while len(unique) > k:
            unique[arr[i]] -= 1
            if unique[arr[i]] == 0:
                del unique[arr[i]]
            i += 1
        count = max(count, j - i + 1)        
    
    print(count)