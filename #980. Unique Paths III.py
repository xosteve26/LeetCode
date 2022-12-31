class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        startRow, startCol = 0, 0
        visit = set()
        steps = [0]
        result = [0]

        def dfs(row, col):
            #Edge conditions of the grid, obstacle detection & repeated visit.
            if row >= ROW or col >= COL or col < 0 or row < 0 or grid[row][col] == -1 or (row, col) in visit:
                return 0

            #Calculate each step taken, if the point we are at is the end and if we've taken the required number of steps
            #then we remove that step and increment our result by 1
            steps[0] += 1
            if grid[row][col] == 2:
                if steps[0] == totalSteps:
                    steps[0] -= 1
                    result[0] += 1
                    return
                else:
                    steps[0] -= 1
                    return

            #Add the valid co-ordinate to the visited set
            visit.add((row, col))

            #Iterate through all 4 directions of a coordinate
            directions = [[row+1, col], [row-1, col],
                          [row, col+1], [row, col-1]]
            for nr, nc in directions:
                dfs(nr, nc)

            #Backstrack your steps by removing the step from the counter and the corordinate from the visited set.
            steps[0] -= 1
            visit.remove((row, col))
            return

        #Identify the number of obstacles in the grid so that was we can calculate the number of steps that are required to be taken and also identify the starting co-ordinates.
        obs = 0
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == -1:
                    obs += 1
                if grid[r][c] == 1:
                    startRow, startCol = r, c

        #Calculate the required number of steps that needs to be taken by subtracting the number of obstacles from the      total co-ordinates.
        totalSteps = (ROW*COL)-obs
        dfs(startRow, startCol)
        return result[0]
