
def findRestaurant(list1, list2):
    """
    :type list1: List[str]
    :type list2: List[str]
    :rtype: List[str]
    """
    l = set(list1).intersection(set(list2)) 
    d = { e : i for i,e in enumerate(list1) if e in l }
    for i, e in enumerate(list2) : 
        if e in l : d[e] = d[e] + i 
        
    minval= min(d.values())
    res = [ k for k, v in d.items() if minval == v] 
    return res
        

list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["KFC","Burger King","Tapioca Express","Shogun"]

# list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
# list2 = ["KFC","Shogun","Burger King"]
print(findRestaurant(list1, list2))
