class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        visit = set()
        posDiag = set()
        negDiag = set()

        result = []
        board = [['.'] * n for _ in range(n)]

        def nQueens(row):
            if row == n:
                copyBoard = [''.join(r) for r in board]
                result.append(copyBoard)
                return

            for col in range(n):
                if col in visit or (row+col) in posDiag or (row-col) in negDiag:
                    continue

                visit.add(col)
                posDiag.add(row+col)
                negDiag.add(row-col)
                board[row][col] = "Q"

                nQueens(row+1)

                board[row][col] = "."
                visit.remove(col)
                posDiag.remove(row+col)
                negDiag.remove(row-col)

        nQueens(0)
        return result
