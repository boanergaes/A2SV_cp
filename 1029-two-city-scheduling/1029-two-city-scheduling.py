class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        costs.sort(key=lambda x : abs(x[0] - x[1]), reverse=True)
        cost = a = b = 0

        for i in range(n):
            if a < n//2 and b < n//2:
                if costs[i][0] < costs[i][1]:
                    cost += costs[i][0]
                    a += 1
                else:
                    cost += costs[i][1]
                    b += 1
            elif a < n//2:
                cost += costs[i][0]
                a += 1
            elif b < n//2:
                cost += costs[i][1]
                b += 1
        
        return cost