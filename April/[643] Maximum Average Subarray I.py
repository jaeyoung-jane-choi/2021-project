def findMaxAverage(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: float
    """
    
    maxavg = sumval = sum(nums[0:k])
    for i in range(k, len(nums)):
        sumval = sumval + nums[i] - nums[i-k] 
        if  sumval > maxavg : maxavg = sumval 
            
    return maxavg/k




nums = [1,12,-5,-6,50,3]
k = 4

nums = [5]
k=1

nums = [0,1,1,3,3]
k=4
print(findMaxAverage(nums, k))