from collections import Counter

def minDeletions(s):
    """
    :type s: str
    :rtype: int
    """
    freq = Counter(s)
    res, seen = 0, set()
    for k in freq.values() : 
        while k in seen : 
            k-=1
            res+=1 
        if k : seen.add(k)
    return res 

s = 'aaabbbcc'
print(minDeletions(s))