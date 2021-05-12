
def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    current= maxsum = nums[0]
    for i in nums[1:]: 
        current = max(i, current+i)
        maxsum = max(maxsum, current)
    return maxsum


nums = [-2,1,-3,4,-1,2,1,-5,4]
print( maxSubArray(nums))