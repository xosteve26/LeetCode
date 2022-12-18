class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW,COL=len(board), len(board[0])
        visit=set()

        def dfs(r,c,idx):
            if idx==len(word):
                return True

            if(r<0 or c<0 or r>=ROW or c>=COL or (r,c) in visit 
                or board[r][c]!=word[idx]):
                return False
            
            visit.add((r,c))
    
            if(dfs(r+1,c, idx+1) or dfs(r-1,c,idx+1) or dfs(r,c+1, idx+1) or
               dfs(r, c-1, idx+1)):
                return True
            visit.remove((r,c))
            return False

        for r in range(ROW):
            for c in range(COL):
                if(board[r][c]==word[0] and dfs(r,c,0)):
                    return True
        return False