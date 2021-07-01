def containsCloseNums(nums, k):
    if not nums : return False 
    
    h = {}    
    for i, n in enumerate(nums) : 
        if n in h : 
            if abs(h[n] - i ) <= k : return True 
            else:  
                del h[n]
                h[n] = i 
        else: h[n] =  i 
    
    return False  
