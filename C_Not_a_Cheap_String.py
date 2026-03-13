def mag(c):
    return ord(c) - ord('a') + 1

t = int(input())

for _ in range(t):
    s = input()
    n = len(s)
    p = int(input())
    idx = []
    psum = [0]
    for i in range(n):
        toadd = psum[-1]
        m = mag(s[i])
        if toadd + m <= p:
            idx.append(i)
            toadd += m
        psum.append(toadd)
        
    res = []
    for i in idx:
        res.append(s[i])
        
    print(''.join(res))