class Solution:
    def networkDelayTime(self, times: List[List[int]], length: int, k: int) -> int:
        
        adjList={i:[] for i in range(length+1)}
        
        for s,d,w in times:
            adjList[s].append((d,w))
            
        result=0
        shortest={}
        minHeap=[(0,k)]
        
        while minHeap:
            w,n=heapq.heappop(minHeap)
            
            if n in shortest:
                continue   
                
            shortest[n]=w
            result=max(result,w)
            
            for node,weight in adjList[n]:
                if node not in shortest:
                    heapq.heappush(minHeap,(w+weight, node))
        
        return result if len(shortest)==length else -1
        