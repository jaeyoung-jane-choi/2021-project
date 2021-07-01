def lemonadeChange(bills):
    """
    :type bills: List[int]
    :rtype: bool
    """
    change = [0,0] 
    for b in bills: 
        if b == 5 :
            change[0] +=1 
            
        elif b == 10 and change[0]> 0: 
            change[0] -= 1 
            change[1] +=1 
                
        elif b==20 and change[0] > 0 and change[1] >0  : 
            change[0] -=1 
            change[1] -=1
            
        elif b==20 and change[0] > 3 :
            change[0] -= 3 
             
             
        else: return False 
    
    return True  


lemonadeChange([5,5,5,10,5,5,10,20,20,20])
