def areAlmostEqual(s1, s2):
    """
    :type s1: str
    :type s2: str
    :rtype: bool
    """
    # if s1 ==s2 : return True 
    # res =[]
    # for i in range(len(s1)) : 
    #     if s1[i] != s2[i] : res.append((s1[i], s2[i])) 
    # if len(res) != 2 : return False 
    # return res[0][0] == res[1][1] and res[0][1] == res[1][0]
    diff = [[x,y] for x,y in zip(s1,s2) if x != y]
    return not diff or len(diff) == 2 and diff[0][::-1] == diff[1]




s1 = "bank"  
s2 = "kanb"
s1 = "npv"
s2 = "zpn"
print(areAlmostEqual(s1,s2))