
def maxCount(m, n, ops):
    """
    :type m: int
    :type n: int
    :type ops: List[List[int]]
    :rtype: int
    """
    if not ops :
        return m*n 
    # x,y = zip(*ops)
    # return min(x)*min(y)
    return min(o[0] for o in ops) * min(o[1] for o in ops)
        
m = 3
n = 3
ops = [[2,2],[3,3]]

# m, n =3,3 
# ops  = [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]]
print(maxCount(m, n, ops))