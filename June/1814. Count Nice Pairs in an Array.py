 
import collections


def countNicePairs(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    res ,cnt = 0, collections.Counter()
    for a in nums : 
        b = int(str(a)[::-1])
        res += cnt[a-b] 
        cnt[a-b] +=1  
    return res % (10**9 + 7)
    


nums = [42,11,1,97]
nums = [13,10,35,24,76]
print(countNicePairs(nums)) 