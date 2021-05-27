def specialArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums= sorted(nums)
    for l in range(len(nums)+1)[::-1] : 
        cnt = 0 
        for k in nums[::-1] : 
            if k >= l : cnt+=1 
            else: break 
        if l == cnt : return l 
    return -1 
        



nums = [0,4,3,0,4 ]
nums = [3,6,7,7,0]
print( specialArray(nums))