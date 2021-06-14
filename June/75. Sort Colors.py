
def sortColors(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    start, mid, last = 0 , 0 , len(nums)-1 
    while mid <= last: 
        if nums[mid] == 0 : 
            nums[start], nums[mid] = nums[mid], nums[start]
            start, mid = start+1 , mid +1 
        elif nums[mid] == 2 : 
            nums[mid], nums[last] = nums[last], nums[mid]
            last-=1 
        else: #==1 
            mid+=1 
    return nums 

nums = [2,0,2,1,1,0]
print(sortColors(nums))
