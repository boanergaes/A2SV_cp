n = int(input())

positions = list(map(int, input().split()))

max_speeds = list(map(int, input().split()))

def valid(time):
    max_left = 0
    min_right = float('inf')
    
    for i in range(n):
        can_go = max_speeds[i] * time
        max_left = max(max_left, positions[i] - can_go)
        min_right = min(min_right, positions[i] + can_go)
    
    return max_left <= min_right

low = 0
high = 10 ** 9

while low <= high:
    mid = low + (high - low) / 2
    if valid(mid):
        high = mid - 10 ** -6
    else:
        low = mid + 10 ** -6
        
print(low)