n, k = map(int, input().split())
arr = list(map(int, input().split()))

diffs = [arr[i] - arr[i-1] for i in range(1, n)]
diffs.sort(reverse=True)

# tot cost: cost if we had only 1 segment,
#  tot_cost == sum(diffs)
tot_cost = arr[-1] - arr[0]

# when you divide the arr at i, you cut lose the cost of arr[i] - arr[i-1] 
# sorting diffs lets you find k-1 pts with maximum return (highest cost to cut lose)
highest_costs = sum(diffs[:k-1])

# minimum cost = tot cost - highest costs
print(tot_cost - highest_costs)