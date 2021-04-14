def sortArrayByParity(A):
    """
    :type A: List[int]
    :rtype: List[int]
    """
    A= sorted(A,key = lambda x : x%2)
    return A 

A= [3,1,2,4]
print(sortArrayByParity(A))