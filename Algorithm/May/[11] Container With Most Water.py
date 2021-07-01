


def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """

    #O(n^2)
    # mx = 0 
    # for i in range(len(height)):
    #     for j in range(i+1, len(height)) :
    #         tot = abs(j-i)* min(height[i] , height[j]) 
    #         mx = max(mx,tot)
    # return mx

    i , j , water = 0, len(height) -1 , 0 
    while i < j: 
        water = max(water, (j-i)*min(height[i],height[j]))
        if height[i] < height[j] : i +=1 
        else : j -=1 
    return water
        



    
height= [1,8,6,2,5,4,8,3,7]
# height = [1,2,1]
# height = [1,1]
# height= [2,3,4,5,18,17,6]
print(maxArea(height))