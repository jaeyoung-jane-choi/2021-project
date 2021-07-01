def findLengthOfLCIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    maxlen =res = 0 
    for i in range(len(nums)-1) : 
        if nums[i] < nums[i+1] : maxlen +=1 
        else: maxlen = 0
        res = max(maxlen,res)

    return res+1
        


nums = [1,3,5,4,7]
nums = [2,2,2,2]
nums =  [1,3,5,4,2,3,4,5]
print(findLengthOfLCIS(nums))