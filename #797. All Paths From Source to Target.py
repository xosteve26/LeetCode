class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        LENGTH = len(graph)

        #DFS traversal to find all the paths from the first node to the last node
        def dfs(node, path):
            path.append(node)

            #If the node is the last node, add the path to the result
            if node == LENGTH-1:
                result.append(path[:])

            #Recursively visit all the neighbours of the node
            for neighbour in graph[node]:
                dfs(neighbour, path)
            #Remove the node from the path
            path.pop()

        #Start the recursion from the first node
        dfs(0, [])
        return result
