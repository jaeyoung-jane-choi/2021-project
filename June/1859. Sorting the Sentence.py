import re 
def sortSentence(s):
    """
    :type s: str
    :rtype: str
    """
    d= {}
    for word in s.split(' ') :
        n, w = re.findall('\d', word)[0] , re.findall('\D*', word)[0]
        d[n] = w 
    
    return ' '.join([v for k,v in sorted(d.items(), key= lambda x : x[0] ) ] )
        
        
    
s = "Myself2 Me1 I4 and3"
s= "z1 z2 z3"
print(sortSentence(s))