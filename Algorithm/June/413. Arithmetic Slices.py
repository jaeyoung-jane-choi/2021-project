 
def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    curr = res = 0 
    for i in range(2, len(nums)) :
        if nums[i] - nums[i-1] == nums[i-1] - nums[i-2] : 
            curr +=1 
            res +=curr 
        else : curr = 0 
    return res 

nums = [1,2,3,4]
print(numberOfArithmeticSlices(nums))