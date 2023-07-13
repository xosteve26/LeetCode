class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, t in enumerate(tasks):
            t.append(i)

        tasks.sort(key = lambda task: task[0])
        res= []
        t, heap = 0, []
        i=0

        while heap or i<len(tasks):
            while(i<len(tasks) and tasks[i][0]<=t):
                heapq.heappush(heap, (tasks[i][1], tasks[i][2]))
                i+=1

            if not heap:
                t = tasks[i][0]
            else:
                procTime, idx = heapq.heappop(heap)
                res.append(idx)
                t+=procTime

        return res
