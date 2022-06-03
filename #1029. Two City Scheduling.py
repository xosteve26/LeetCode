class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        difference = []
        minimum = 0
        for i in costs:
            difference.append([i[1] - i[0], i[0], i[1]])

        difference.sort()
        for j in range(len(costs)):
            if(j < len(costs) // 2):
                minimum += difference[j][2]
            else:
                minimum += difference[j][1]
        return minimum
