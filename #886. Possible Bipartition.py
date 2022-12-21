class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:

        def isBipartite(start):
            queue = deque()
            queue.append(start)
            color[start] = 1

            while queue:
                LENGTH = len(queue)
                for _ in range(LENGTH):
                    node = queue.pop()

                    for neighbour in adjList[node]:
                        if color[neighbour] == color[node]:
                            return False
                        if color[neighbour] == -1:
                            color[neighbour] = 1-color[node]
                            queue.append(neighbour)

            return True

        adjList = defaultdict(list)

        #Creating the adjacency list
        for i in range(len(dislikes)):
            adjList[dislikes[i][0]].append(dislikes[i][1])
            adjList[dislikes[i][1]].append(dislikes[i][0])

        color = [-1]*(n+1)
        #Iterate through each node
        for i in range(n+1):
            #If node isn't visited then we check if that node along with its neighbours form a bipartite graph
            if color[i] == -1:
                if(not isBipartite(i)):
                    return False

        return True
