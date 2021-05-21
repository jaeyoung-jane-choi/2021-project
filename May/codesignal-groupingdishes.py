def groupingDishes(dishes):
    h  , res = {} , []
    for d in dishes : 
        food = d[0]
        for e in range(1, len(d)): 
            if d[e] in h : h[d[e]].append(food)
            else: h[d[e]] = [food]
            
    
    i =0 
    for k, v in h.items() :
        if len(v) > 1 :  
            res.append([k])
            res[i].extend(sorted(v))
            i +=1 
    
    return sorted(res) 
    
