n = int(input())
string = input()
q = []

for i in range(n):
    if q and q[-1] != string[i]:
        q.pop()
    else:
        q.append(string[i])

print(len(q))