class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = [0]
        visit = set()

        def helper(r, c):

            if r >= len(grid) or r < 0 or c >= len(grid[0]) or c < 0 or grid[r][c] == 0:
                perimeter[0] += 1
                return

            if (r, c) in visit:
                return

            visit.add((r, c))

            helper(r, c+1)
            helper(r+1, c)
            helper(r, c-1)
            helper(r-1, c)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j] == 1):
                    helper(i, j)
                    return perimeter[0]
