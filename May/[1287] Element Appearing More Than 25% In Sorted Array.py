
from collections import Counter 
def findSpecialInteger(arr):
    """
    :type arr: List[int]
    :rtype: int
    """
    return Counter(arr).most_common(1)[0][0]


arr = [1,2,2,6,6,6,6,7,10]
print( findSpecialInteger(arr) ) 