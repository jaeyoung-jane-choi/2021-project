def maxProduct(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums = sorted(nums,reverse=True)
    return (nums[0]-1)*(nums[1]-1)
        
nums = [1,5,4,5]
print(maxProduct(nums))