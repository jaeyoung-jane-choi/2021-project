from collections import defaultdict
def isIsomorphic(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    d = defaultdict(str)
    if len(set(s))!=len(set(t)): return False 

    for i, j in zip(s, t): 
        if not d[i] : d[i] = j 
        if d[i] != j : return False 
        
    return True 

    # one-liner
    # return len(set(zip(s, t))) == len(set(s)) == len(set(t))


s = 'egg'
t = 'add'
s = "paper"
t = "title"
s= "badc"
t= "baba"
s = "bbbaaaba"
t = "aaabbbba"
print(isIsomorphic(s, t))