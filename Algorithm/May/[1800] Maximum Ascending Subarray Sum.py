
def maxAscendingSum(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    res = maxsum = 0 
    for i in range(len(nums)) : 
        if i==0 or nums[i-1] < nums[i] : maxsum += nums[i]
        else: maxsum =nums[i]
        res = max(res, maxsum )
    return res 

    
    


nums = [10,20,30,5,10,50]
# nums = [12,17,15,13,10,11,12]

print(maxAscendingSum(nums))