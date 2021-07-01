def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    if numRows == 1 : return [[1]] 
    res = [0]*(numRows)
    res[0], res[1]  = [1], [1,1]
    for i in range(2,numRows) :  
        l = [res[i-1][k] + res[i-1][k+1]  for k in range(len(res[i-1])-1)] 
        res[i] = [1] + l + [1]
    return res 




numRows = 5 
numRows = 2
print(generate(numRows))