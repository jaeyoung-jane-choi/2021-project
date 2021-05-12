
def thirdMax(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums = set(nums)
    if len(nums) < 3 : return max(nums)
    return sorted(nums,reverse=True)[2]


nums = [2,2,3,1]
print(thirdMax(nums))