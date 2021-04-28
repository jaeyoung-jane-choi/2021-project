def isValidSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    big = set()
    for i in range(0,9) :
        for j in range(0,9):
            if board[i][j]!= '.' : 
                curr = board[i][j]
                if (i,curr) in big or (curr,j) in big or (i/3,j/3,curr) in big : return False 
                big.add((i,curr))
                big.add((curr,j))
                big.add((i/3,j/3,curr))
            
    return True 


board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(isValidSudoku(board))