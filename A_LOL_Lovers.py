from collections import Counter, defaultdict

n = int(input())
items = input()

tot_count = Counter(items)
my_count = defaultdict(int)

for i in range(n-1):
    my_count[items[i]] += 1
    if my_count['L'] != tot_count['L'] - my_count['L'] and my_count['O'] != tot_count['O'] - my_count['O']:
        print(i+1)
        break
else:
    print(-1)