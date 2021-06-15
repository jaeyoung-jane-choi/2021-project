 

def updateMatrix(mat):
    """
    :type mat: List[List[int]]
    :rtype: List[List[int]]
    """
    res =[[10000*x for x in row] for row in mat]
    for _ in range(4):
        for row in res :
            for j in range(1, len(row)):  row[j] = min(row[j], row[j-1]+1) 
        res = list(map(list, zip(*res[::-1])))
                 
    return res 
mat = [[0,0,0],[0,1,0],[1,1,1]]
print(updateMatrix(mat))