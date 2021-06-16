def minFlips(target):
    """
    :type target: str
    :rtype: int
    """
    flip, stat = 0, '0'
    for t in target:
        if t!= stat : 
            flip+=1 
            stat = '0' if stat =='1' else '1'
    return flip 
    
target = "10111"
print(minFlips(target))