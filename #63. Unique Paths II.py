class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        d = {}

        def helper(r, c):
            if (r, c) in d:
                return d[(r, c)]

            if(r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0])):
                return 0

            if(grid[r][c] == 1):
                return 0

            if(r == len(grid)-1 and c == len(grid[0])-1):
                return 1

            d[(r, c)] = helper(r+1, c)+helper(r, c+1)
            return d[(r, c)]

        return helper(0, 0)
