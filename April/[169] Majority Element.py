
from collections import Counter

def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    
    return Counter(nums).most_common(1)[0][0]
    




nums = [3,2,3]
print(majorityElement(nums))