n = int(input())

inp = [list(map(int, input().split())) for _ in range(n)]

def findIndexes(inp):
    inp.sort(key=lambda x : x[0])
    i = 0
    j = 1
    while j < len(inp):
        if  (inp[i][0] >= inp[j][0] and inp[i][1] <= inp[j][1]):
            return (i+1, j+1)
        # if (inp[i][0] <= inp[j][0] and inp[i][1] >= inp[j][1]):
        #     return (j+1, i+1)
        if inp[j][1] > inp[i][1]:
            
    return (-1, -1)

sol = findIndexes(inp)
print(sol[0], sol[1])
    