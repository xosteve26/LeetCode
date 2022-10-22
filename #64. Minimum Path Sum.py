class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        res = [[float("inf")]*(COL+1) for _ in range(ROW+1)]

        res[ROW][COL-1] = 0

        for r in range(ROW-1, -1, -1):
            for c in range(COL-1, -1, -1):
                res[r][c] = grid[r][c]+min(res[r][c+1], res[r+1][c])

        return res[0][0]
