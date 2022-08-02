import heapq


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        for row in (matrix):
            heap.extend(row)

        heapq.heapify(heap)
        while heap and k != 0:
            res = heapq.heappop(heap)
            k -= 1

        return res
