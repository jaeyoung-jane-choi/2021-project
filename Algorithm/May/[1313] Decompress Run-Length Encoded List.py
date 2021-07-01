
def decompressRLElist(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    res = []
    for i, j in zip(nums[::2], nums[1::2]): res.extend([j]*i)
    return res 
nums = [1,2,3,4]
nums = [1,1,2,3]
print( decompressRLElist(nums))