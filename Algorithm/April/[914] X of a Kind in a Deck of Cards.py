from collections import Counter
# from math import gcd
from functools import reduce

def gcd(a,b):
    while b: a,b = b, a%b 
    return a 

def hasGroupsSizeX(deck):
    """
    :type deck: List[int]
    :rtype: bool
    """
    
    l = Counter(deck).values()    
    return reduce(gcd, l) > 1  

    


deck = [1,2,3,4,4,3,2,1]
# deck =[1,1,1,2,2,2,3,3]
# deck = [1,1]
deck = [1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3]
print(hasGroupsSizeX(deck))