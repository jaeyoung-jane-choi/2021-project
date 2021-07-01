
def numSubseq(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    nums.sort()
    l, r = 0, len(nums)-1
    res, mod = 0, 19**9+7
    while l <= r : 
        if nums[l] + nums[r] > target: r-=1 
        else: 
            res+= pow(2,r-l,mod) # 2**r-l % mod 
            l+=1 
    return res % mod 



nums = [3,5,6,7]
target = 9
print(numSubseq(nums, target))