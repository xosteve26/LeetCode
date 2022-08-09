import heapq
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        res = []
        heap = []
        d = {}
        for i in score:
            heap.append(-i)

        heapq.heapify(heap)

        for i in range(len(heap)):
            if i == 0:
                d[abs(heapq.heappop(heap))] = "Gold Medal"
            elif i == 1:
                d[abs(heapq.heappop(heap))] = "Silver Medal"
            elif i == 2:
                d[abs(heapq.heappop(heap))] = "Bronze Medal"
            else:
                d[abs(heapq.heappop(heap))] = str(i+1)

        for i in score:
            res.append(d[i])

        return res
