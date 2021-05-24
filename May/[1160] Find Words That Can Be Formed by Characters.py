def countCharacters( words, chars):
    """
    :type words: List[str]
    :type chars: str
    :rtype: int
    """ 
    h, res = {}, []
    for c in chars :
        if c in h : h[c] +=1 
        else: h[c] =1  
 
    for w in words:  
        copy, flag = h.copy()  , True  
        for l in w : 
            if l in copy and copy[l] >= 1 : copy[l] -=1 
            else : flag = False  
        if flag== True : res.append(w)
        
    return sum( len(c) for c in res ) 





words = ["cat","bt","hat","tree"]
chars = "atach"
print(countCharacters(words, chars))