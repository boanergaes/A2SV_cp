n = int(input())
bananas = list(map(int, input().split()))
split = [0, 0]
min_diff = float('inf')

def backtrack(i):
    global min_diff
    if i == n:
        min_diff = min(min_diff, abs(split[0] - split[1]))
        return
    for j in range(2):
        split[j] += bananas[i]
        backtrack(i+1)
        split[j] -= bananas[i]
    
backtrack(0)
print(min_diff)