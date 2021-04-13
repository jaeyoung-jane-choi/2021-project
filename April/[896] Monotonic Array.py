def isMonotonic(A):
    """
    :type A: List[int]
    :rtype: bool
    """
    # return sorted(A) in (A, A[::-1])
    return A == sorted(A) or A == sorted(A, reverse=True) 
    

A= [1,2,2,3]
A= [6,5,4,4]
A= [1,3,2]
print(isMonotonic(A))