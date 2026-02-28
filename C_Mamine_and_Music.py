n, k = map(int, input().split())

arr = list(map(int, input().split()))

idx = {}
for i in range(len(arr)):
    idx[arr[i]] = idx.get(arr[i], set()) | {i}
    
arr.sort()
inst = 0
days = 0
indices = []
i = 0
while i < n and days + arr[i] <= k:
    inst += 1
    days += arr[i]
    indices.append(str(idx[arr[i]].pop() + 1))
    i += 1
    
print(inst)
print(' '.join(indices))