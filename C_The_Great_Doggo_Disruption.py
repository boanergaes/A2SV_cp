from collections import Counter

def solution(colors):
    if len(colors) == 1:
        return 'Yes'
    for c in colors:
        if c > 1:
            return 'Yes'
    return 'No'

n = int(input())
colors = Counter(input()).values()

print(solution(colors))
