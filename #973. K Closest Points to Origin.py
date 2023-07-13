class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def euclidianDistance(point):
            xSquare = (0 - point[0]) ** 2
            ySquare = (0 - point[1]) ** 2
            return math.sqrt(xSquare + ySquare)

        heap = []
        for point in points:
            heapq.heappush(heap, (euclidianDistance(point), point))

        KClosestPoints = []
        while heap and k:
            KClosestPoints.append(heapq.heappop(heap)[1])
            k-=1

        return KClosestPoints