class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visit = set()
        LENGTH = len(rooms)

        #DFS traversal to visit all the rooms
        def dfs(node):
            #If the node has already been visited, return
            if node in visit:
                return
            #Add the node to the visited set
            visit.add(node)

            #Recursively visit all the neighbours of the node as long as they haven't been visited
            for neighbour in rooms[node]:
                if neighbour not in visit:
                    dfs(neighbour)
            #If all the neighbours have been visited,
            return

        #Start the recursion from the first room
        dfs(0)
        #If the number of visited rooms is equal to the number of rooms, return True, else return False
        return len(visit) == LENGTH
