
def smallerNumbersThanCurrent(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    dct ={}
    for i, n in enumerate(sorted(nums)):
        if n not in dct: 
            dct[n] = i 
    return [dct[n] for n in nums]

nums = [8,1,2,2,3]
print(smallerNumbersThanCurrent(nums))