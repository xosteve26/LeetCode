class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        
        heap=[]
        result=0
        i=0
        fuel=startFuel
        distance=0
        while fuel < target:
            
            while i<len(stations) and fuel >=stations[i][0]:
                heapq.heappush(heap,-stations[i][1])
                i+=1
                
            if not heap:
                return -1
            
            gas=heapq.heappop(heap)
            fuel+=-gas
            result+=1
                          
        return result
