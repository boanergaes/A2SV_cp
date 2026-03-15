n = int(input())
positions = map(int, input().split())

print(sorted(positions)[(n-1) // 2])