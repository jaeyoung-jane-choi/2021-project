

def diagonalSum(mat):
    """
    :type mat: List[List[int]]
    :rtype: int
    """
    i= res = 0 
    while i < len(mat) :
        res+=mat[i][i]
        if i != len(mat)-i-1:  res += mat[i][len(mat)-i-1]
        i+=1
    return res 



mat = [[1,2,3],
    [4,5,6],
    [7,8,9]]

print(diagonalSum(mat))