def matrixReshape(mat, r, c):
    """
    :type mat: List[List[int]]
    :type r: int
    :type c: int
    :rtype: List[List[int]]
    """
    if r*c != len(mat)* len(mat[0]) : return mat 
    else: 
        items = [y for x in mat for y in  x ]
        return [items[x*c : ((x+1)*c)] for x in range(r)]
    



mat = [[1,2],[3,4]]
r = 1
c = 4
print(matrixReshape(mat, r, c))