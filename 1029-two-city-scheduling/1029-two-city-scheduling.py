class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        costs.sort(key=lambda x : x[0] - x[1])
        cost = 0
        for i in range(n//2):
            cost += costs[i][0]
        for i in range(n//2, n):
            cost += costs[i][1]
        return cost