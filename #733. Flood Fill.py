class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROW, COL = len(image), len(image[0])
        original = image[sr][sc]
        visit = set()

        def dfs(r, c):
            print(r, c)
            if(r < 0 or r == ROW or c < 0 or c == COL or image[r][c] != original or (r, c) in visit):
                return False
            visit.add((r, c))
            image[r][c] = color

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

            return True

        dfs(sr, sc)
        return image
