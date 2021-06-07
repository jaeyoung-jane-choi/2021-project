def balancedStringSplit(s):
    """
    :type s: str
    :rtype: int
    """
    w_cnt = l_cnt = r_cnt = 0 
    for l in s : 
        if l == 'L': l_cnt+=1 
        else : r_cnt+=1 
        if l_cnt == r_cnt : w_cnt+=1 
    return w_cnt

s = "RLRRLLRLRL"
print(balancedStringSplit(s))