
from collections import defaultdict
def countLargestGroup(n):
    """
    :type n: int
    :rtype: int
    """
    dic = defaultdict(int)    
    for i in range(1,n+1):
        a = sum(map(int, list(str(i))))
        dic[a]+=1

    maxval = max(dic.values())
    return len([v for v in dic.values()  if v == maxval ])

    
    
    
    



n=46
n=13
n = 125
print(countLargestGroup(n))