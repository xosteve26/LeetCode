class Solution:
    def frequencySort(self, s: str) -> str:
        if len(s) == 1:
            return s

        freq = Counter(s)
        result = ''
        heap = []
        heapq.heapify(heap)
        for k, v in freq.items():
            heapq.heappush(heap, (-v, k))

        while heap:
            c = heapq.heappop(heap)
            result += (c[1]*abs(c[0]))

        return result
