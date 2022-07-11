class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        end = len(cost)-2
        cost.append(0)
        while end >= 0:
            cost[end] = min(cost[end]+cost[end+1], cost[end]+cost[end+2])
            end -= 1

        return min(cost[0], cost[1])
