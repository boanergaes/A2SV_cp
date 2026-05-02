t = int(input())

for _ in range(t):
    n = int(input())
    
    # conquered = [False] * n
    enemy = list(input())
    abel = list(input())
    count = 0
    
    for i in range(n):
        if abel[i] == '0':
            continue
        
        if enemy[i] == '0':# and not conquered[i]:
            count += 1
            # conquered[i] = True
            enemy[i] = '2'
            continue
            
        if i%2 == 0:
            if i < n - 1 and enemy[i+1] == '1':
                count += 1
                enemy[i+1] = '2'
                # conquered[i+1] = True
            elif i > 0 and enemy[i-1] == '1':
                enemy[i-1] = '2'
                count += 1
        else:
            if i > 0 and enemy[i-1] == '1':
                enemy[i-1] = '2'
                count += 1
            elif i < n - 1 and enemy[i+1] == '1':
                enemy[i+1] = '2'
                count += 1
                
    print(count)            