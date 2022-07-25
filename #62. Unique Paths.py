class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        matrix = [[-1 for j in range(n)]for i in range(m)]
        cache = {}

        def helper(r, c):
            if (r, c) in cache:
                return cache[(r, c)]
            if r == m-1 and c == n-1:
                return 1
            if(r >= m or c >= n):
                return 0

            cache[(r, c)] = helper(r+1, c) + helper(r, c+1)

            return cache[(r, c)]

        return helper(0, 0)
