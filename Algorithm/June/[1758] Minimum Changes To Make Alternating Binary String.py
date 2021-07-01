
def minOperations(s):
    """
    :type s: str
    :rtype: int
    """
    res = sum(i%2 == int(c) for i, c in enumerate(s) ) 
    return min(res,len(s)-res)
            
         

s= '1111'
s = '0100'
s = "10010100"
print(minOperations(s))