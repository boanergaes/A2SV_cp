matrix = [input().split() for i in range(5)]
n = 5 # given in the problem

row = 0
column = 0
for i in range(n):
    for j in range(n):
        if matrix[i][j] == '1':
            row = i
            column = j
    
print(abs(row - 2) + abs(column - 2))