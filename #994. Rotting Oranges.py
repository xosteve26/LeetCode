class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        time, fresh = 0, 0
        queue = deque()
        visit = set()
        for i in range(ROW):
            for j in range(COL):
                if(grid[i][j] == 1):
                    fresh += 1
                elif(grid[i][j] == 2):
                    queue.append((i, j))

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while queue and fresh > 0:
            for i in range(len(queue)):
                R, C = queue.popleft()

                for cr, cc in directions:
                    row, col = cr+R, cc+C

                    if(row < 0 or col < 0 or row >= ROW or col >= COL or grid[row][col] != 1 or (row, col) in visit):
                        continue

                    visit.add((row, col))
                    grid[row][col] = 2
                    queue.append((row, col))
                    fresh -= 1
            time += 1

        return time if fresh == 0 else -1
