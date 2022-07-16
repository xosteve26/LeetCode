
def findPaths(m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
    memo = {}

    def recursion(r, c, moves):
        if (r, c, moves) in memo:
            return memo[(r, c, moves)]

        if r < 0 or r >= m or c < 0 or c >= n:
            return 1

        if moves == 0:
            return 0

        d1 = recursion(r+1, c, moves-1)
        d2 = recursion(r-1, c, moves-1)
        d3 = recursion(r, c+1, moves-1)
        d4 = recursion(r, c-1, moves-1)
        memo[(r, c, moves)] = d1+d2+d3+d4

        return d1+d2+d3+d4

    return recursion(startRow, startColumn, maxMove) % (10**9+7)


print(findPaths(1,3,3,0,1))

