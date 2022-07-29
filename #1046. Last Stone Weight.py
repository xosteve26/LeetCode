import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            heaviest = heapq.heappop(stones)
            sHeavy = heapq.heappop(stones)

            if abs(heaviest) > abs(sHeavy):
                heapq.heappush(stones, heaviest-sHeavy)
                print(stones)

        return 0 if not stones else abs(stones[0])
