n=4
board=[['.' for i in range(n)]for j in range(n)]
print(board)
l=['a','b','v','d','e','f']
x=list(enumerate(l))
print(x)
def n_queens(board,row):
    if row == len(board):
        display(board)
        return 1

    count=0
    for col in range(n):
        if(isSafe(board,row,col)):
            board[row][col] ='Q'
            count+=n_queens(board,row+1)
            board[row][col] = '.'

    return count


def display(board):
    for i in board:
        print(i)

def isSafe(board,row,col):
    #check vertical row
    for a in range(row):
        if(board[j][col] == 'Q'):
            return False

    #Diagonal Left
    maxLeft=min(row,col)
    for b in range(1,maxLeft+1):
        if(board[row-b][col-b] == 'Q'):
            return False

    #Diagonal Right
    
    
