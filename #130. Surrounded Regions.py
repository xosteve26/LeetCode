class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROW, COL = len(board), len(board[0])

        visit = set()

        def dfs(r, c):
            if (r, c) in visit:
                return
            if(r < 0 or r == ROW or c < 0 or c == COL or board[r][c] == 'X' or board[r][c] == 'T'):
                return

            board[r][c] = 'T'

            visit.add((r, c))

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        #Capture regions @ Border and dfs them to arbitrary value 'T'
        for R in range(ROW):
            for C in range(COL):
                if(board[R][C] == 'O' and ((R in [0, ROW-1]) or (C in [0, COL-1]))):
                    dfs(R, C)

        #Remainig Os are changed to X cuz they're the ones left out that are surrounded by water
        for R in range(ROW):
            for C in range(COL):
                if board[R][C] == 'O':
                    board[R][C] = 'X'
        #Change the arbitrary value T back to O
        for R in range(ROW):
            for C in range(COL):
                if board[R][C] == 'T':
                    board[R][C] = 'O'

        return board
