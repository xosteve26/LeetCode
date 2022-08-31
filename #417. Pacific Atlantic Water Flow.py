class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pset = set()
        aset = set()

        ROW, COL = len(heights), len(heights[0])

        def dfs(r, c, visit, prevHeight):
            if((r, c) in visit or r < 0 or c < 0 or r == ROW or c == COL or
                    heights[r][c] < prevHeight):
                return

            visit.add((r, c))

            dfs(r+1, c, visit, heights[r][c])
            dfs(r, c+1, visit, heights[r][c])
            dfs(r-1, c, visit, heights[r][c])
            dfs(r, c-1, visit, heights[r][c])

        for c in range(COL):
            dfs(0, c, pset, heights[0][c])
            dfs(ROW-1, c, aset, heights[ROW-1][c])

        for r in range(ROW):
            dfs(r, 0, pset, heights[r][0])
            dfs(r, COL-1, aset, heights[r][COL-1])

        result = []
        for r in range(ROW):
            for c in range(COL):
                if (r, c) in aset and (r, c) in pset:
                    result.append([r, c])

        return result
