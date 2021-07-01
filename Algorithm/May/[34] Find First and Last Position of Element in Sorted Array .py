def searchRange(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    low , high = 0, len(nums)-1 
    while low <= high : 
        mid = (low+high)//2 
        if nums[low] == target and nums[high] == target : return [low, high] 

        if nums[mid] > target : high = mid -1 
        elif nums[mid] < target : low = mid + 1 
        else:
            if nums[low] != target : low = low+1 
            if nums[high]!= target : high = high-1   
    return [-1,-1]





    
nums = [5,7,7,8,8,10]
target = 8
nums = [1]
target = 1 
print(searchRange(nums, target))