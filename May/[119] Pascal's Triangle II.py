
def getRow(rowIndex):
    """
    :type rowIndex: int
    :rtype: List[int]
    """
    # r= [[]for _ in range(rowIndex+1)]
    # r[0] = [1] 
 
    # for i in range(1,len(r)) :  
    #     j= 0
    #     r[i].append(1)
    #     while j < len(r[i-1]) -1  :
    #         r[i].append(r[i-1][j] + r[i-1][j+1] ) 
    #         j+=1
    #     r[i].append(1)

    # return r[rowIndex]
    
    row = [1]
    for _ in range(rowIndex) : 
        row = [x+y for x,y in zip([0]+row, row+[0])]
    return row 

rowIndex = 3
print(getRow(rowIndex))