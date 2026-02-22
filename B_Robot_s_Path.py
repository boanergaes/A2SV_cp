n, k = map(int, input().split())

road = list(input())
consecutive_obstacles = 0

for i in range(n):
    if road[i] == '.':
        consecutive_obstacles = 0
        continue
    consecutive_obstacles += 1
    if consecutive_obstacles == k:
        print('NO')
        break
else:
    print('YES')