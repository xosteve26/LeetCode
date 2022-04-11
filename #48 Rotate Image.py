class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        length=len(matrix)
        for i in range(length):
            l=[]
            for j in range(length):
                move=(length-1)-j
                l.append(matrix[move][i])
            matrix.append(l)
  
        for remove in range(length):
            popped=matrix.pop(0)