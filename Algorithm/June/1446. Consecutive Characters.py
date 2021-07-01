import itertools 
def maxPower(s):
    """
    :type s: str
    :rtype: int
    """
    # curr , cnt, maxcnt = s[0] , 0 , 0 
    # for w in s[1:] :
    #     if w == curr: cnt+=1 
    #     else:            
    #         maxcnt = max(cnt, maxcnt)
    #         curr , cnt = w  , 0
    # return max(cnt, maxcnt) +1  
    return max(len(list(b)) for a, b in itertools.groupby(s))

        

s= 'leetcode'
print(maxPower(s))