n = int(input())
inp = list(map(int, input().split(' ')))
s = sorted(inp, reverse=True)

idx = {}
for i, val in enumerate(s):
    if val not in idx:
        idx[val] = i + 1
        
out = []
for k in inp:
    out.append(str(idx[k]))
    
print(' '.join(out))