 
def getNoZeroIntegers(n):
    """
    :type n: int
    :rtype: List[int]
    """
    for i in range(1, int(n/2)+1) : 
        if '0' not in str(i)  and '0' not in str(n-i) : return [i,n-i]  
    

n=1010 
print(getNoZeroIntegers(n))