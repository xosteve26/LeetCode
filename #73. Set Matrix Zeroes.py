class Solution:
    def setZeroes(self, grid: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeroRow = False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j] == 0):
                    grid[0][j] = 0

                    if i > 0:
                        grid[i][0] = 0
                    else:
                        zeroRow = True

        for r in range(1, len(grid)):
            for c in range(1, len(grid[0])):
                if(grid[0][c] == 0 or grid[r][0] == 0):
                    grid[r][c] = 0

        if grid[0][0] == 0:
            for r in range(len(grid)):
                grid[r][0] = 0

        if zeroRow:
            grid[0] = [0 for _ in range(len(grid[0]))]
