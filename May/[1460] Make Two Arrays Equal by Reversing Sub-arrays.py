
def canBeEqual(target, arr):
    """
    :type target: List[int]
    :type arr: List[int]
    :rtype: bool
    """
    return sorted(target ) == sorted(arr) 





target = [1,2,3,4]
arr = [2,4,1,3]
print(canBeEqual(target, arr))