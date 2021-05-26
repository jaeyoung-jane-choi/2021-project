def hasAlternatingBits(n):
    """
    :type n: int
    :rtype: bool
    """ 
    for i, j in zip(bin(n)[2:], bin(n)[2:][1:]) : 
        if i==j: return False  
    return True 

print(hasAlternatingBits(7))