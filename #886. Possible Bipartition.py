class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:

        def isBipartite(start):
            #Create an empty queue for BFS traversal.
            queue = deque()
            #Append the starting node into the queue and mark that node with 1 in the color array.
            queue.append(start)
            color[start] = 1

            while queue:
                LENGTH = len(queue)
                #Iterate throughout the length of the queue and extract each inserted node from it in each iteration.
                for _ in range(LENGTH):
                    node = queue.pop()

                    #Iterate through all of the neighbours of our above extracted node .
                    for neighbour in adjList[node]:
                        #if the neighbour's color matches the color of our extracted node then they are in the same set which breaks the bipartite graph property and therefore they cant be placed in seperate sets.
                        if color[neighbour] == color[node]:
                            return False
                        #However if the neighbour's color is equal to '-1', then we haven't visited it, therefore we color an opposing color to that of our current node and append it to the queue such that we can process its neighbours at a lator point.
                        if color[neighbour] == -1:
                            color[neighbour] = 1 if color[node] == 2 else 2
                            queue.append(neighbour)

            return True

        adjList = defaultdict(list)

        #Creating the adjacency list
        for i in range(len(dislikes)):
            adjList[dislikes[i][0]].append(dislikes[i][1])
            adjList[dislikes[i][1]].append(dislikes[i][0])

        #Graph coloring array [-1: Unprocessed, 1: Set 1, 0: Set 2 ]
        color = [-1]*(n+1)
        #Iterate through each node
        for i in range(n+1):
            #If node isn't visited then we check if that node along with its neighbours form a bipartite graph
            if color[i] == -1:
                if(not isBipartite(i)):
                    return False

        return True
