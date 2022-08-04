import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for i in nums:
            heap.append(-i)

        heapq.heapify(heap)
        for i in range(k):
            large = heapq.heappop(heap)

        return -(large)
