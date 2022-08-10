import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            d[str(i)] = 1 + d.get(str(i), 0)

        print(d)
        heap = [(-freq, element) for element, freq in d.items()]
        heapq.heapify(heap)

        result = [heapq.heappop(heap)[1] for _ in range(k)]
        return result
