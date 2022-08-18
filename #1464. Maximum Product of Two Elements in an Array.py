import heapq
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        heap = []
        for i in nums:
            heap.append(-i)

        heapq.heapify(heap)
        max1 = heapq.heappop(heap)
        max2 = heapq.heappop(heap)

        return (abs(max1)-1)*(abs(max2)-1)
