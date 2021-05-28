def bitwiseComplement(n):
    """
    :type n: int
    :rtype: int
    """
    b = bin(n)[2:]
    k= ''.join(['0' if b[i] =='1' else '1' for i in range(len(b))  ]) 
    i, res = len(k)-1 , 0 
    for e in k:  
        if e == '1' : res+= int(e)*(2**int(i))
        i -=1 
    return res




n =5
print(bitwiseComplement(n))