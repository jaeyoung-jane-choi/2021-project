def possibleSums(coins, quantity):
    possibleSums ={0}
    for c, q in zip(coins, quantity) : 
        possibleSums = {x+(c*i) for x in possibleSums for i in range(q+1)}
    return len(possibleSums) -1 