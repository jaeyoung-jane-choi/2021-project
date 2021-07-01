def fairCandySwap(A, B):
    """
    :type A: List[int]
    :type B: List[int]
    :rtype: List[int]
    """
    diff =(sum(A) - sum(B))/ 2
    A, B = set(A), set(B)
    for b in B: 
        if diff+ b in A:
            return [diff+b,b]



# A = [1,1]
# B = [2,2]
A = [1,2]
B = [2,3]

print(fairCandySwap(A, B))