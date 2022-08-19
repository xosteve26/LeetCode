class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda t: t[1])
        cap = 0
        heap = []
        heapq.heapify(heap)

        for i in trips:
            c, start, end = i

            while heap and start >= heap[0][0]:
                trip = heapq.heappop(heap)
                cap -= trip[1]

            cap += c

            if cap > capacity:
                return False

            heapq.heappush(heap, (end, c))

        return True
