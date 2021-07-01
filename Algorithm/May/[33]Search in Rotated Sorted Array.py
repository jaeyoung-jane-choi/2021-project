
def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    # low, high = 0, len(nums)-1 
    # while low < high : 
    #     mid = (low+high)/2 

    #     #^ : XOR  ; 0,0,0 & 1,1,1 -> FALSE
    #     if (nums[0] > target)^ (nums[0] > nums[mid]) ^ (target > nums[mid]) : low = mid + 1 
    #     else :   high = mid 

    # return low if target in nums[low:low+1] else -1 

    low, high = 0, len(nums)-1 
    while low <= high :
        mid = (low+high) //2 
        if nums[mid] == target : return mid 
        if nums[0] <= target < nums[mid] or target < nums[mid] < nums[0] or nums[mid] < nums[0] <= target:  hi = mid -1 
        else: low = mid+1 
    return -1 
    