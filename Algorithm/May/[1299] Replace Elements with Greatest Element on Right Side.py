
def replaceElements(arr):
    """
    :type arr: List[int]
    :rtype: List[int]
    """
    res,maxval = [-1],0
    for n in arr[::-1]:
        if n > maxval : maxval = n
        res.append(maxval)
    return res[::-1][1:]
        
    
arr = [17,18,5,4,6,1]
arr = [400]
print(replaceElements(arr))