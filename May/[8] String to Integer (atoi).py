
def myAtoi(s):
    """
    :type s: str
    :rtype: int
    """
    s, l = s.strip(' '), []

    if len(s) == 0:  return 0
    
    if s[0] == '-' : 
        m = -1 
        s= s[1:]
    elif s[0] == '+' : 
        m = 1 
        s = s[1:]
    else :  m = 1 
        
        
    for num in list(s): 
        if num.isdigit() : l.append(num)
        else : break 

    if len(l) == 0 : res = 0 
    else: res = m* int(''.join(l)) 


    return max(-2**31, min(res,2**31-1))
    
s = "-4193 with words"
s= '-91283472332'
s = "words and 987"
s = "21474836460"
s = '   -42'
print(myAtoi(s))