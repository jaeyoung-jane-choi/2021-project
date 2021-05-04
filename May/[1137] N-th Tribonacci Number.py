
def tribonacci(n):
    """
    :type n: int
    :rtype: int
    """
    if n ==0 : return 0 
    elif n in [1,2]: return 1 
    memo = [0]*(n+1)
    memo[0], memo[1],memo[2] = 0, 1 , 1
    

    for i in range(3,n+1):
        memo[i]= memo[i-3] + memo[i-2] + memo[i-1]
        
    return memo[n]
    
        #SIMPLE 
    # a, b, c = 1, 0, 0
    # for _ in xrange(n): a, b, c = b, c, a + b + c
    # return c

n = 25
print(tribonacci(n))