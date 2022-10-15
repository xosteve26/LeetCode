class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        visit=set()
        result=0
        ROW,COL=len(matrix), len(matrix[0])
        dp={}
        
        def recursion(r,c,prev):
            if r<0 or c<0  or r>=ROW or c>=COL or matrix[r][c]<=prev:
                return 0
            
            if (r,c) in dp:
                return dp[(r,c)]
        
            prev=matrix[r][c]
            count=1
                
            count=max(count,1+recursion(r+1,c, prev))
            count=max(count,1+recursion(r,c-1, prev))
            count=max(count,1+recursion(r-1,c, prev))
            count=max(count,1+recursion(r,c+1, prev))
            
            dp[(r,c)]=count
            return dp[(r,c)]
             
        
        
        for R in range(ROW):
            for C in range(COL):
                possible_result=recursion(R,C,-1)
                result=max(result, possible_result)
                
        return result