def transpose(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[List[int]]
    """
    
    res, i = [], 0
    for i in range(len(matrix[0])): 
        j, element = 0 ,[]        
        for j in range(len(matrix)) : 
            element.append(matrix[j][i])
            j+=1  

        res.append(element)
    return res




#easier answer 
def transpose(matrix):
    return list(map(list, zip(*matrix)))





matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(transpose(matrix))