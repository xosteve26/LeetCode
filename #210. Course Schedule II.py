class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adjList={i:[] for i in range(numCourses)}
        visit=set()
        result=[]
        path=set()
        for a,b in prerequisites:
            adjList[a].append(b)
        
        def dfs(node):
            if node in visit:
                return True
            
            if node in path:
                return False
            
            path.add(node)
            for neighbour in adjList[node]:
                if not dfs(neighbour):
                    return False  
                
            path.remove(node)    
            visit.add(node)
            result.append(node)
            return True

        for i in range(numCourses):
            if not dfs(i):return []
        return result
        
        
        