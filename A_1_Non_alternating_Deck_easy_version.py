t = int(input())

for _ in range(t):
    n = int(input()) - 1
    
    alice = 1
    bob = 0
    flag = True
    i = 2
    while n - (i + i + 1) > 0:
        if flag:
            bob += i + i + 1
        else:
            alice += i + i + 1
        n -= i + i + 1
        i += 2
        flag = not flag
    if flag:
        bob += n
    else:
        alice += n
        
    print(alice, bob)