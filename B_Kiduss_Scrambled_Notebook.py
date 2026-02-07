t = int(input())
for _ in range(t):
    s = input()
    for i in range(1, len(s)):
        first = s[:i]
        second = s[i:]
        if int(first) < int(second) and second[0] != '0':
            print(first, second)
            break
    else:
        print(-1)