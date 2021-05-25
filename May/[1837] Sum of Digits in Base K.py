def sumBase(n, k):
    """
    :type n: int
    :type k: int
    :rtype: int
    """ 
    res = []
    while n >= k  :
        m,r = divmod(n,k)
        res.append(r)
        n = m 
    res.append(n)
    return sum(res)


n,k = 34,6 
n, k =10,10
print(sumBase(n,k))