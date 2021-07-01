def arraySign(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if 0 in nums : return 0 
    cnt = sum(1 for num in nums if num < 0 )
    return -1 if cnt%2!=0 else 1 
        






nums = [-1,-2,-3,-4,3,2,1]
# nums = [1,5,0,2,-3]
nums = [-1,1,-1,1,-1]
print(arraySign(nums))