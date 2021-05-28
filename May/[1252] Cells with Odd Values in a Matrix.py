def oddCells(m, n, indices):
    """
    :type m: int
    :type n: int
    :type indices: List[List[int]]
    :rtype: int
    """
    x, y = [0]*m , [0]*n
    for r,c in indices : 
        x[r] +=1 
        y[c] +=1   
    
    return sum([(r+c)%2 for c in y for r in x])


m = 2
n = 3
indices = [[0,1],[1,1]]
print(oddCells(m, n, indices))