 
def missingNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    # for nn in range(n+1) :  #O(N)Space 
    #     if nn not in nums : return nn 
    return ((n*(n+1))//2) - sum(nums)


nums = [9,6,4,2,3,5,7,0,1]
print(missingNumber(nums))
    