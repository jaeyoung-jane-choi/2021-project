

def firstNotRepeatingCharacter(s):
    # h = {}
    # for i, a in enumerate(s): 
    #     if a not in h : h[a] = [i,1]
    #     else: h[a][1] +=1
    
    # minidx, keyval = len(s), '_'
    # for k,v in h.items() : 
    #     if v[1] == 1 and minidx > v[0] : minidx, keyval = v[0], k
        
    # return keyval

    for c in s: 
        if s.index(c) == s.rindex(c): return c
    return '_'