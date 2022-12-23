class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        #Initialize hash map to store the visited nodes with a boolean value to denote whether the node is safe or not.
        hashMap = {}

        def dfs(node):
            #The node that were trying to traverse thorugh, if its present in the hash map then we return its value so as to not end up in a cycle.
            if node in hashMap:
                return hashMap[node]

            #Initialize each node's value to False at first.
            hashMap[node] = False

            #Iterate through each nodes neighbours if any of them return a False in the subsequent recursion then return a False.
            for neighbour in graph[node]:
                if not dfs(neighbour):
                    return False
            #If we manage to iterate through all the neighbours of a node and not run into any cycles(False) then we can say that particular node is a safe node and denote it with a True in the hash map.
            hashMap[node] = True
            return True

        #Result Array to store all the nodes that are safe
        result = []
        for j in range(len(graph)):
            if dfs(j):
                result.append(j)

        return result
