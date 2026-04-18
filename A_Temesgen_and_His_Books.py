from collections import deque

t = int(input())

def backtrack(i):
        global res
        global piles
        
        if i == n:
            if piles[0] and piles[1]:
                res = max(res, pages[piles[0][0]] + pages[piles[1][0]])
            return
        
        for j in range(2):
            buff = deque()
            while piles[j] and piles[j][-1] < i:
                buff.appendleft(piles[j].pop())
            piles[j].append(i)
            backtrack(i+1)
            piles[j].pop()
            piles[j].extend(buff)

for _ in range(t):
    n = int(input())
    
    pages = list(map(int, input().split()))
    res = 0
    piles = [deque(), deque()]
    
    backtrack(0)
    
    print(res)

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    print(max(arr[:n-1]) + arr[-1])