from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())
    stick_freq = Counter(input().split())
    polygons = 0

    for freq, val in stick_freq.items():
        if val >= 6:
            polygons += val // 3
        elif val >= 3:
            polygons += 1
            
    print(polygons)