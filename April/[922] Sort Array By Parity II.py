


def sortArrayByParityII(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """

    nums.sort(key= lambda x: x %2 )
    
    res=[]
    for a,b in zip(nums[:len(nums)//2], nums[len(nums)//2:]):
        res.append(a)
        res.append(b)
    return res 

nums  = [4,2,5,7]
nums = [3,4]
print(sortArrayByParityII(nums))