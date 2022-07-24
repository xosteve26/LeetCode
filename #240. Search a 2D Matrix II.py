class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def binary_Search(row):
            l = 0
            r = len(row)-1

            while l <= r:
                mid = (l+r) // 2
                if row[mid] == target:
                    return True
                elif row[mid] < target:
                    l = mid+1
                else:
                    r = mid-1
            return False

        for i in matrix:
            res = binary_Search(i)
            if res:
                return res