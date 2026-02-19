t = int(input())

for _ in range(t):
    m, s = map(int, input().split())
    nums = list(map(int, input().split()))
    
    n = max(nums)
    curr_sum = sum(nums)
    while n*(n+1)/2 - curr_sum < s:
        n += 1
      
    if n*(n+1)/2 - curr_sum == s:
        print('YES')
    else:
        print('NO')