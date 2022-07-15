class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        visit = set()
        max_area = 0

        def dfs(R, C):
            if(R < 0 or R == ROW or C < 0 or C == COL or grid[R][C] == 0 or (R, C) in visit):
                return 0

            visit.add((R, C))

            return (1 + dfs(R+1, C) + dfs(R-1, C) + dfs(R, C+1) + dfs(R, C-1))

        for row in range(ROW):
            for col in range(COL):
                max_area = max(max_area, dfs(row, col))

        return max_area
