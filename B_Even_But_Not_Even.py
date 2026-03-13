t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    arr = list(s)
    tot = sum(map(int, arr))
    
    while arr and not (int(arr[-1]) % 2 != 0 and tot % 2 == 0):
        tot -= int(arr.pop())
        
    if arr:
        print(''.join(arr))
    else:
        print(-1)