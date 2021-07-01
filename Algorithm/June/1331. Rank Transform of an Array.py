 
from re import I


def arrayRankTransform(arr):
    """
    :type arr: List[int]
    :rtype: List[int]
    """
    d= {e : i+1 for i, e in enumerate(sorted(set(arr))) } 

    return [ d[e] for e in arr ] 



arr= [40,10,20,30,10]
arr = [37,12,28,9,100,56,80,5,12]
print(arrayRankTransform(arr))