class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left = 0
        right = len(matrix[0])
        top = 0
        bottom = len(matrix)
        result = []
        while top < bottom and left < right:

            #Top row
            for i in range(left, right):
                result.append(matrix[top][i])
            top += 1

            #Last Column
            for i in range(top, bottom):
                result.append(matrix[i][right-1])
            right -= 1

            if not(left < right and top < bottom):
                break

            #Last Row
            for i in range(right-1, left-1, -1):
                result.append(matrix[bottom-1][i])
            bottom -= 1

            #First Col Except first matrix cell
            for i in range(bottom-1, top-1, -1):
                result.append(matrix[i][left])

            left += 1

        return result
