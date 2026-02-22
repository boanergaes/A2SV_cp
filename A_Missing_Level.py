n = int(input())
levels = list(map(int, input().split()))
tot_levels = sum(levels)

print(n*(n+1)//2 - tot_levels)