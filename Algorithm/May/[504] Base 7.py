def convertToBase7(num):
    """
    :type num: int
    :rtype: str
    """
    res, flag =[] , False 
    if num < 0 : num , flag = -num, True 
    
    while num >= 7 :
        m,r= divmod(num, 7)
        res.append(str(r))
        num = m 
    res.append(str(num))  
    if flag == True :  return '-'+''.join(res[::-1]) 
    return ''.join(res[::-1])
    


num = -7 
# num =100 
print(convertToBase7(num ))