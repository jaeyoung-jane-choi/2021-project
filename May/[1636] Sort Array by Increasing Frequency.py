
from collections import Counter 
def frequencySort(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    cnt= Counter(nums) 
    l= sorted(cnt, key = lambda x : (cnt[x], -x ))   

    res = []
    for i in l : 
        c = cnt[i] 
        while c > 0: 
            res.append(i)
            c-=1 
    
    return res 
nums = [1,1,2,2,2,3]
nums = [2,3,1,3,2]
# nums = [-1,1,-6,4,5,-6,1,4,1]
print(frequencySort(nums))