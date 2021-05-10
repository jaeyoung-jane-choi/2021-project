
def minSubsequence(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    nums = sorted(nums,reverse=True)
    for i in range(1,len(nums)):
        if sum(nums[:i]) > sum(nums[i:]) : return nums[:i]
        # print(sum(nums[:i]) , sum(nums[i:]))
    return nums 
        


nums = [4,3,10,9,8]

# nums = [4,4,7,6,7]
# nums =[6]
print(minSubsequence(nums))