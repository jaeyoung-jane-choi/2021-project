def numWaterBottles(numBottles, numExchange):
    """
    :type numBottles: int
    :type numExchange: int
    :rtype: int
    """
    
    t ,res = numBottles , [numBottles]
    while t //numExchange : 
        m , r  = t//numExchange, t%numExchange
        res.append(m)
        t = m+r
        
        
        
    return sum(res)
        
numBottles= 2
numExchange = 3
print(numWaterBottles(numBottles, numExchange))