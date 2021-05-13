
def removeElement( nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    
    # for n in range(nums.count(val)): nums.remove(val)
    # print(nums)
    # return len(nums)

    start  ,end = 0, len(nums)-1 
    while start <= end: 
        if nums[start] == val : nums[start], nums[end], end = nums[end], nums[start], end - 1
        else : start +=1 
    print(nums)
    return start

nums = [3,2,2,3]
val = 3
print(removeElement( nums, val))