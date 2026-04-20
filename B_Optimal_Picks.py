t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    items = sorted(map(int, input().split()), reverse=True)
    
    eve = 0
    noah = 0
    
    for i in range(n):
        if i % 2 == 0:
            eve += items[i]
            continue
        
        if k == 0:
            noah += items[i]
            continue
        
        if items[i-1] >= items[i] + k:
            noah += items[i] + k
            k = 0            
        else:
            noah += items[i-1]
            k -= items[i-1] - items[i]
    
    print(eve - noah)