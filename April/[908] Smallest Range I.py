def smallestRangeI(A, K):
    """
    :type A: List[int]
    :type K: int
    :rtype: int
    """

    A= sorted(A)
    if len(A)==1 : return 0 
    for k in range(1, K+1) : 
        if A[0] + k == A[-1]: return 0 
        elif A[0]+k > A[-1]-k : return 0 

    return (A[-1]-K)-(A[0]+K)

    #easier version 
    # return max(0, max(A) - min(A) - 2 * K)



A = [0,10]
K = 2 

A = [1,3,6]
K = 3

A= [1,3,6]
K= 3
print(smallestRangeI(A, K))