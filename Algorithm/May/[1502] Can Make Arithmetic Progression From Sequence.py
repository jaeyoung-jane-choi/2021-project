def canMakeArithmeticProgression(arr):
    """
    :type arr: List[int]
    :rtype: bool
    """
    arr = sorted(arr)
    diff= arr[1]- arr[0]
    for i in range(1, len(arr)-1) :  
        if arr[i] + diff != arr[i+1] : return False 
    return True 


arr = [3,5,1]
arr = [1,2,4]
arr = [-4,-2,0]
print(canMakeArithmeticProgression(arr))