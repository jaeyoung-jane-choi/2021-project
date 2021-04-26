def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    #BRUTE_FORCE 
    # profit = 0
    # for i in range(len(prices)):
    #     for k in prices[i:]:
    #         if k - prices[i] > profit:
    #             profit = k - prices[i]
        
    # o(n)
    profit, min_price = 0, float('inf')
    for price in prices :
        min_price = min(price,min_price)
        profit = max(profit, price -min_price )
    return profit

prices = [7,1,5,3,6,4]
# prices=[7,6,4,3,1]
prices = [7,3,8,1,2]
print(maxProfit(prices))