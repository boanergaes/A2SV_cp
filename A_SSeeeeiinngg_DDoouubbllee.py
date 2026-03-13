t = int(input())

for _ in range(t):
    s = input()
    n = len(s)
    pal = [''] * (2*n)
    
    for i in range(n):
        pal[i] = s[i]
        pal[2*n - 1 - i] = s[i]
        
    print(''.join(pal))