def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    if n == 1 : return 1 

    res = [0 for i in range(n)]
    res[0], res[1] = 1,2 
    
    for i in range(2,n):
        res[i] = res[i-1] + res[i-2]
    return res[-1]
    

n = 2 
print(climbStairs(n))