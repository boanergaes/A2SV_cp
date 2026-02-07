n = int(input())

for _ in range(n):
    s = input()
    
    if '**' in s or '*<' in s or '>*' in s or '><' in s:
        print(-1)
        continue

    left = s.count('<')
    right = s.count('>')
    no_current = s.count('*')
    print(max(left + no_current, right + no_current))