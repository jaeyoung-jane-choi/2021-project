
def isSubsequence(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    for l in s :
        i = t.find(l)
        if i == -1 : return False 
        else: t = t[i+1:]
    return True 
        

    

s = "abc"
t = "ahbgdc"

# s = "aaaaaa"
# t = "bbaaaa"

# s= "b"
# t= "c"
print(isSubsequence(s, t))