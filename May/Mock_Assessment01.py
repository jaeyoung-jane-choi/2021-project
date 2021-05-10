
def isOneBitCharacter(bits):
    """
    :type bits: List[int]
    :rtype: bool
    """
    i, res=0, 0
    while i < len(bits) :
        if bits[i:i+2] == [1,1] or bits[i:i+2] == [1,0] : 
            res = 2 
            i+=2 
        elif bits[i] == 0 : 
            res = 1 
            i+=1
            
    return res == 1 

bits = [1, 1, 1, 0]
bits = [0,0]
bits = [0,1,0]
print(isOneBitCharacter(bits))