 
import enum


def shortestToChar(s, c):
    """
    :type s: str
    :type c: str
    :rtype: List[int]
    """
    n , pos = len(s), -float('inf')
    res = [n]* n 
    
    for i in list(range(n)) + list(range(n)[::-1]) : 
        if s[i] == c : pos = i 
        res[i] = min(res[i], abs(i-pos))
    return res 

s = "loveleetcode"
c = "e"
print(shortestToChar(s, c))