

from collections import Counter

def buddyStrings(a, b):
    """
        :type a: str
        :type b: str
        :rtype: boolL
    """
    #prerequisite 
    if len(a)!= len(b): return False 

    if a == b : return False  if len(a) == len(set(a)) else True 
    
    diff = [(i,j) for i,j in zip(a,b) if i!= j]
    return True  if len(diff) == 2  and diff[0] == diff[1][::-1] else False 


a = "aaaaaaabc"
b = "aaaaaaacb"

# a= 'aa'
# b= 'aa'

# a= "abc"
# b= 'bca'
        
print(buddyStrings(a,b))