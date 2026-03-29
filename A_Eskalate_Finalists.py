k = int(input())
ranks = list(map(int, input().split()))
ranks.sort()
missing = ranks[0] - 1

for i in range(1, k):
    missing += ranks[i] - ranks[i-1] - 1
if ranks[-1] < 25:
    missing += 25 - ranks[-1]

print(missing - (25 - k))