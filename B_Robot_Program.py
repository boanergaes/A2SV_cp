t = int(input())

for _ in range(t):
    n, x, k = map(int, input().split())
    cmd = input()
    zero_count = 0
    second = 0
    
    i = 0
    while i < len(cmd) and second < k:
        if cmd[i] == 'L':
            x -= 1
        elif cmd[i] == 'R':
            x += 1
        i += 1
        if x == 0:
            i = 0
            zero_count += 1
        
        second += 1
    
    print(zero_count)
