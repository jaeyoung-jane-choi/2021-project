
def halvesAreAlike(s):
    """
    :type s: str
    :rtype: bool
    """
    fr , se = s[:len(s)//2] , s[len(s)//2:]
    
    return check(fr) == check(se)
    

def check(s):
    vow = ['a','e','i','o','u']
    cnt = 0 
    for c in s: 
        if c.lower() in vow : cnt+=1 
    return cnt 




s= 'book'
s = "AbCdEfGh"
s = "MerryChristmas"
print(halvesAreAlike( s))