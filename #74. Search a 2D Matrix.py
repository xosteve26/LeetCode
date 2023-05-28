class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        START,END = 0, len(matrix)-1

        #Identify the row where the target lies.
        TARGET_ROW_INDEX = None
        while START<=END:
            midRow=(START+END)//2
            if(target>=matrix[midRow][0] and target<=matrix[midRow][-1]):
                TARGET_ROW_INDEX=midRow
                break
            elif(target<matrix[midRow][0]):
                END=midRow-1
            else:START=midRow+1

        #If the TARGET_ROW_INDEX is not found then its None, which means the the target isn't within the range between the start element and the last element in the matrix.
        if TARGET_ROW_INDEX==None: return False

        #Perform binary search on the target row to identify the target element.
        START,END=0,len(matrix[TARGET_ROW_INDEX])-1
        TARGET_ROW = matrix[TARGET_ROW_INDEX]
        while START<=END:
            mid=(START+END)//2
            if(TARGET_ROW[mid] == target):
                return True
            elif(target>TARGET_ROW[mid]):
                START=mid+1
            else: END=mid-1

        return False