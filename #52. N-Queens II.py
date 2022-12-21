class Solution:
    def totalNQueens(self, n: int) -> int:
        visit = set()
        posDiag = set()
        negDiag = set()

        board = [['.'] * n for _ in range(n)]

        def nQueens(row, result):
            if row == n:
                return result+1

            for col in range(n):
                if col in visit or (row+col) in posDiag or (row-col) in negDiag:
                    continue

                visit.add(col)
                posDiag.add(row+col)
                negDiag.add(row-col)
                board[row][col] = "Q"

                result = nQueens(row+1, result)

                board[row][col] = "."
                visit.remove(col)
                posDiag.remove(row+col)
                negDiag.remove(row-col)

            return result

        return nQueens(0, 0)
