def weight(c):
    return ord(c) - ord('a') + 1

n, k = map(int, input().split())
layers = list(input())
layers.sort()
cake_weight = weight(layers[0])
k -= 1

for i in range(1, n):
    if k == 0:
        break
    curr = weight(layers[i])
    prev = weight(layers[i-1])
    if curr - prev > 1:
        cake_weight += curr
        k -= 1
        
print(cake_weight if k == 0 else -1)

