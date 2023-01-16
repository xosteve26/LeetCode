class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        visit = set()
        noOfLandCells = 0

        #DFS traversal to convert the border 1 nodes and its connecting nodes into an arbitrary value "G" to signify that we can walk off from this path.
        def dfs(r, c):
            visit.add((r, c))
            grid[r][c] = "G"

            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for new_row, new_col in directions:
                nr = r+new_row
                nc = c+new_col

                if(nr < ROW and nc < COL and nr >= 0 and nc >= 0
                        and (nr, nc) not in visit
                        and grid[nr][nc] == 1):
                    dfs(nr, nc)

        #Convert the path from border nodes to connecting nodes into an arbitrary value of "G".
        for row in range(ROW):
            for col in range(COL):
                if(row == 0 or row == ROW-1 or col == 0 or col == COL-1):
                    if(grid[row][col] == 1):
                        dfs(row, col)

        #Count the nodes that aren't 0s or Gs because they are nodes that cant be used to walk off.
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    noOfLandCells += 1

        return noOfLandCells
