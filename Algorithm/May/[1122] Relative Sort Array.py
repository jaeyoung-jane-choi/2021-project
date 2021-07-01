
def relativeSortArray(arr1, arr2):
    """
    :type arr1: List[int]
    :type arr2: List[int]
    :rtype: List[int]
    """
    d= {}
    for i, e in enumerate(arr2) :  d[e] = i
        
    return sorted(arr1, key = lambda x : d[x] if x in d else x+len(arr1)) 


arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]

arr1 = [26,21,11,20,50,34,1,18]
arr2 = [21,11,26,20]

print(relativeSortArray(arr1,arr2))