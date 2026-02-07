t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    
    if '2026' in s or '2025' not in s:
        print(0)
    elif '2025' in s:
        print(1)
        