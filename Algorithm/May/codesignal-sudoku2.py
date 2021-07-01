def sudoku2(grid):
    val = set()
    for i in range(9):
        for j in range(9) : 
            if grid[i][j] != '.' : 
                current = grid[i][j]
                if (i,current) in val or (current, j) in val or (current, i//3 , j//3 ) in val: return False 
                val.add((i,current))
                val.add((current,j))
                val.add((current, i//3, j//3))    
    return True 

