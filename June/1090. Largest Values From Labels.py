 
import collections


def largestValsFromLabels(values, labels, num_wanted, use_limit):
    """
    :type values: List[int]
    :type labels: List[int]
    :type num_wanted: int
    :type use_limit: int
    :rtype: int
    """
    d = collections.defaultdict(int)
    cnt = res = 0 
    for v,l in sorted(zip(values, labels),reverse=True):
        if cnt == num_wanted : break 
        if d[l] == use_limit : continue 
        cnt+=1 
        res+= v 
        d[l]+=1 
    print(sorted(zip(values, labels),reverse=True))
    return res
        



values = [5,4,3,2,1]
labels = [1,3,3,3,2]
num_wanted = 3
use_limit = 2
print(largestValsFromLabels(values, labels, num_wanted, use_limit))