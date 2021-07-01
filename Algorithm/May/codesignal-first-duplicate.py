def firstDuplicate(a):
    # hash = {}
    # for element in a : 
    #     if element in hash: return element
    #     else: hash[element] =1 
    # return -1
    mySet=set()
    for el in a:
        if el in mySet:
            return el
        mySet.add(el)
    return -1