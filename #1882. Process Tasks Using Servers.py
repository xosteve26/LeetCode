import heapq
class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        heapServer = []
        for j, s in enumerate(servers):
            heapServer.append([s, j])
        heapq.heapify(heapServer)

        taskProcessor, ans = [], []
        i, t= 0, 0

        while i<len(tasks):
            t= max(i,t)

            if(len(heapServer)==0):
                t = taskProcessor[0][0]
            while taskProcessor and t>=taskProcessor[0][0]:
                taskObject = heapq.heappop(taskProcessor)

                timeOfCompletedTask = taskObject[0]
                taskCompletedServer = taskObject[1][0]
                indexOfServer = taskObject[1][1]

                heapq.heappush(heapServer, [taskCompletedServer, indexOfServer])

            if(heapServer):
                server, idx =  heapq.heappop(heapServer)
                heapq.heappush( taskProcessor, (tasks[i]+t,[server, idx]) )
                ans.append(idx)

            i+=1

        return ans
