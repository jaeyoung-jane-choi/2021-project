
def canPlaceFlowers(flowerbed, n):
    """
    :type flowerbed: List[int]
    :type n: int
    :rtype: bool
    """
    
    flowerbed, x = [0] + flowerbed+ [0], 0
    for i in range(1,len(flowerbed)-1): 
        if flowerbed[i] == 1:  continue 
        if flowerbed[i-1]==0 and flowerbed[i+1]==0 : 
            flowerbed[i] = 1
            x+=1
            
    return x>=n 

    

flowerbed = [1,0,0,0,1]
n = 2
print(canPlaceFlowers(flowerbed, n))