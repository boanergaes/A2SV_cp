t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    score = 0
    
    for i in range(1, 2*n, 2):
        score += min(arr[i-1], arr[i])
    
    print(score)