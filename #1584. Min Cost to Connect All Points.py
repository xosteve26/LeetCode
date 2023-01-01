import heapq
from collections import defaultdict
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        LENGTH = len(points)
        adjList = defaultdict(list)

        #Create an adjacency list with weights
        for coordinates in range(LENGTH):
            x1, y1 = points[coordinates]
            for nextCoordinates in range(coordinates+1, LENGTH):
                x2, y2 = points[nextCoordinates]

                distance = abs(x1-x2) + abs(y1-y2)
                adjList[(x1, y1)].append([distance, (x2, y2)])
                adjList[(x2, y2)].append([distance, (x1, y1)])

        minHeap = []
        #Insert initial edges into the Heap with weights
        for distance, destination in adjList[tuple(points[0])]:
            heapq.heappush(minHeap, [distance, (0, 0), destination])

        minCost = 0
        #Create a set to keep track of visited nodes
        visit = set()
        #Add the first node to the visited set
        visit.add(tuple(points[0]))

        #Run the loop as long elements are present in the heap and visit isn't equal to number of nodes.
        while minHeap and len(visit) != LENGTH:
            #Pop the minimum weight edge from the heap
            wt, src, dst = heapq.heappop(minHeap)

            if dst in visit:
                continue
            #Add the destination node to the visited set
            visit.add(dst)
            #Add the weight to the minimum cost
            minCost += wt
            #Add the edges of the destination node to the heap
            for weight, dstn in adjList[dst]:
                #If the destination node has already been visited, continue
                if dstn in visit:
                    continue
                #Add the edge to the heap
                heapq.heappush(minHeap, [weight, src, dstn])

        return minCost
