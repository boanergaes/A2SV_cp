n = int(input())

for _ in range(n):
    s = input() + '0'
    working = set()
    consec = 1
    for i in range(len(s) - 1):
        if s[i] == s[i+1]:
            consec += 1
            continue
        if consec%2 != 0:
            working.add(s[i])
        consec = 1
        
    print(''.join(sorted(list(working))))
        