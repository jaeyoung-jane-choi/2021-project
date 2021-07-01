
def canThreePartsEqualSum(arr):
    """
    :type arr: List[int]
    :rtype: bool
    """
    totalsum = sum(arr)
    if totalsum % 3 != 0 : return False 
    cnt, cumsum, target = 0, 0 , totalsum//3
    for num in arr: 
        cumsum+= num 
        if cumsum == target : 
            cumsum = 0
            cnt+=1 
    return cnt >=3 

arr = [0,2,1,-6,6,-7,9,1,2,0,1]
print(canThreePartsEqualSum(arr))