
def addToArrayForm(num, k):
    """
    :type num: List[int]
    :type k: int
    :rtype: List[int]
    """   
    for i in range(len(num))[::-1] :  k, num[i] = divmod(num[i] + k , 10 )

    return [int(i) for i in str(k)] + num if k else num
    





num = [1,2,0,0]
k = 34 
print(addToArrayForm(num, k))