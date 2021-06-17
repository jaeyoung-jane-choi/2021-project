import collections
import enum


def peopleIndexes(favoriteCompanies):
    """
    :type favoriteCompanies: List[List[str]]
    :rtype: List[int]
    """ 
    # h = { i : collections.Counter(e) for i , e in enumerate(favoriteCompanies) } 
    # h , res = sorted(h.items(), key = lambda x: len(x[1])) , []
    # for i, e in enumerate(h) : 
    #     n , flag = len(h) -1 , False 
    #     while n > i :  
    #         if e[1]- h[n][1]  == collections.Counter() and n != i : 
    #             flag= True   
    #             break 
    #         n -=1 
    #     if flag == False : res.append(e[0])
    # return sorted(res) 
    
    res , sets = [] , [set(cs) for cs in favoriteCompanies]
    for i, a in enumerate(sets) : 
        for j, b in enumerate(sets) : 
            if i == j : continue 
            if a.issubset(b) : break 
        else: res.append(i)
    return res 


favoriteCompanies = [["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]]
favoriteCompanies = [["leetcode","google","facebook"],["leetcode","amazon"],["facebook","google"]]
print(peopleIndexes(favoriteCompanies))
