class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        visit = set()
        count = 0

        def dfs(R, C):
            if(R < 0 or R == ROW or C < 0 or C == COL or grid[R][C] == '0' or (R, C) in visit):
                return False

            visit.add((R, C))
            dfs(R+1, C)
            dfs(R-1, C)
            dfs(R, C+1)
            dfs(R, C-1)

            return True

        for row in range(ROW):
            for col in range(COL):
                count += 1 if dfs(row, col) else 0

        return count
