t = int(input())

for _ in range(t):
    n, l, r = map(int, input().split())
    arr = list(map(int, input().split()))
    
    wins = 0
    cards = 0
    for a in arr:
        curr = cards + a
        if a >= l and a <= r:
            wins += 1
            cards = 0
            continue
        elif curr < l:
            cards += a
        elif a > r:
            cards = 0
        if cards >= l and cards <= r:
            wins += 1
            cards = 0

    print(wins)