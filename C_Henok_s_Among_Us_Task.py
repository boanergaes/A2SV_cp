a, b = map(int, input().split())
track = []

while int(a) < int(b):
    if b%10 == 1:
        track.append(b)
        b //= 10
    elif b%2 == 0:
        track.append(b)
        b //=2
    else:
        break
track.append(b)

if a != b:
    print('NO')
else:
    print('YES')
    print(len(track))
    for t in track[::-1]:
        print(t, end=' ')
        


        