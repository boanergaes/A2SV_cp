n = int(input())

for _ in range(n):
    s = input()
    l = len(s)
    print('YES' if len(set(s[:l//2])) != 1 else 'NO')