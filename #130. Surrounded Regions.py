class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visit = set()
        ROW, COL = len(board), len(board[0])

        def dfs(r, c):
            board[r][c] = "T"
            visit.add((r, c))

            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for new_row, new_col in directions:
                nr = r+new_row
                nc = c+new_col

                if(nr < ROW and nc < COL and nr >= 0 and nc >= 0 and (nr, nc) not in visit and board[nr][nc] == "O"):
                    dfs(nr, nc)

        #Corrupt nodes that are connected to a border "O" that will not be converted to an "X" by giving them an arbitrary value of "T"
        for i in range(ROW):
            for j in range(COL):
                if(j == 0 or j == COL-1 or i == 0 or i == ROW-1):
                    if(board[i][j] == "O"):
                        dfs(i, j)

        #Convert the Non corrupted nodes["O"] in to an "X" because they aren't connted to a border node.
        for r in range(ROW):
            for c in range(COL):
                if(board[r][c] == "O"):
                    board[r][c] = "X"

        #Convert the arbitrary value "T" back into an "O"
        for r in range(ROW):
            for c in range(COL):
                if(board[r][c] == "T"):
                    board[r][c] = "O"
