def binaryGap(n):
    """
    :type n: int
    :rtype: int
    """
    
    binary = bin(n)[2:]
    l = [ i for i in range(len(list(binary))) if list(binary)[i] =='1']
    if len(l) < 2: return 0

    j, diff=0, 0
    while j+1 < len(l): 
        if abs( l[j] - l[j+1] )  >  diff : 
            diff = abs( l[j] - l[j+1] ) 
        j+=1 

    return diff 
    
#simple version 
def binaryGap(n): 
    index = [i for i, v in enumerate(bin(n)) if v =='1']
    return max([b-a for a,b in zip(index, index[1:])] or [0]) 

print(binaryGap(22)) 

