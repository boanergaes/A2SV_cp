PI = '314159265358979323846264338327'

t = int(input())

for _ in range(t):
    n = input()
    # print(n)
    
    i = 0
    while i < len(n) and PI[i] == n[i]:
        i += 1
        
    print(i)