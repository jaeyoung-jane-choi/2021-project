def reformatNumber(number):
    """
    :type number: str
    :rtype: str
    """
    number = number.replace(' ','').replace('-','')  
    l, i, res = len(number), 0 , [ ]
    while i < l : 
        if i+4 == l : 
            res.append(number[i:i+2])
            i+=2 
        elif i + 3 <= l : 
            res.append(number[i:i+3])
            i += 3
        else : 
            res.append(number[i:i+2])
            i += 2 
            
    if len(res) > 1 : return '-'.join(res)
    return res[0]
    

number = "1-23-45 6"
number = "--17-5 229 35-39475 "
print(reformatNumber(number))