def findMinFibonacciNumbers(k):
    """
    :type k: int
    :rtype: int
    """
    f, cnt = [1,1] , 0 
    while k >= f[-1]:  f.append(f[-1]+ f[-2]) 
    f.pop() 
    while k!= 0 : 
        if k >= f[-1] : 
            k -= f[-1]
            cnt+=1 
        else : f.pop()
    return cnt 


k = 19
print(findMinFibonacciNumbers(k))