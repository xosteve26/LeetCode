class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW,COL=len(grid), len(grid[0])
        visit=set()
        count=0
        
        def dfs(R,C):
            if R<0 or R>=ROW or C<0 or C>=COL or grid[R][C] == '0' or (R,C) in visit:
                return 0
            
            visit.add((R,C))
            
            dfs(R+1,C)
            dfs(R-1,C)
            dfs(R,C+1)
            dfs(R,C-1)
            
            return 1
            
            
        for r in range(ROW):
            for c in range(COL):
                count+=dfs(r,c)
                                  
        return count         