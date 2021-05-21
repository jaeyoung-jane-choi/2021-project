def areFollowingPatterns(strings, patterns):
    
    if  len(set(strings)) == len(set(patterns)) :  
        h = { } 
        for a,b in zip(strings, patterns) : 
            if a in h : 
                if h[a] !=b:  return False 
            else: h[a] = b
        return True 
    else: return False 