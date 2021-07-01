
def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # return len(set(nums))
    for idx in range(len(nums)-1,0,-1):
        if nums[idx] == nums[idx-1]: nums.pop(idx)
        
    return len(nums)

nums = [1,1,2]
nums =  [0,0,1,1,1,2,2,3,3,4]

print(removeDuplicates(nums))