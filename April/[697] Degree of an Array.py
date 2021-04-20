
from collections import defaultdict

from collections import defaultdict
def findShortestSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    d = defaultdict(list)
    for i, n in enumerate(nums): d[n].append(i)
    M = max(len(key) for key in d.values()) 
    return min(max(v)- min(v)+1 for v in d.values() if len(v) == M )
    
# nums = [1,2,2,3,1,4,2]
nums = [1,2,2,3,1]
print(findShortestSubArray(nums))