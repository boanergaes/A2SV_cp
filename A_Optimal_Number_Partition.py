n = int(input())

nums = sorted(map(int, input().split()))

tot = 0
for j in range(n // 2):
    tot += (nums[j] + nums[n - j - 1]) ** 2

print(tot)