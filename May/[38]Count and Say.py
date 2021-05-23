
from itertools import groupby
def countAndSay(n):
    """
    :type n: int
    :rtype: str
    """
    # if n== 1 : return '1'
    # l = ['' for i in range(n)]
    # l[0] , k = '1', 1

    # while k < n  :  
    #     if len(l[k-1]) == 1 : l[k] = '1' + l[k-1]
    #     else :
    #         i = 1
    #         num , cnt = l[k-1][0], 1 
    #         while i  < len(l[k-1]):       
    #             if num == l[k-1][i] : cnt,i = cnt+1 , i+1
    #             else : 
    #                 l[k] += str(cnt)+str(num)
    #                 num,cnt, i = l[k-1][i],1 , i+1
    #         l[k] += str(cnt)+str(num)
    #     k+=1 
    # return l[n-1]

    res = '1'
    for _ in range(n-1): 
        v= ''
        for digit, group in groupby(res) : 
            cnt = len(list(group))
            v += '%i%s' %(cnt, digit)
        res = v 
    return res 


n = 5
print(countAndSay(n))