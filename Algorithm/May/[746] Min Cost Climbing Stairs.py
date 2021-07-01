def minCostClimbingStairs(cost):
    """
    :type cost: List[int]
    :rtype: int
    """
    price = [0] * (len(cost)+1) 
    cost.append(0)
    price[0], price[1] = cost[0], cost[1]
    
    for i in range(2, len(cost)): price[i] = min(price[i-2] + cost[i] , price[i-1] + cost[i] )
        
    return price[-1]
    



cost = [10,15,20]
cost = [1,100,1,1,1,100,1,1,100,1]
print(minCostClimbingStairs(cost))