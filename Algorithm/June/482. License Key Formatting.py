 
def licenseKeyFormatting(s, k):
    """
    :type s: str
    :type k: int
    :rtype: str
    """
    # letter  , res = ''.join(s.upper().split('-')), ''
    # i= cnt= 0 
    # r = len(letter)%k
    # if r!= 0 :  
    #     while r > 0 : res , i, r = res + letter[i] , i+1, r -1 
    #     if i < len(letter)-1 : res+='-' 
    
    # while i < len(letter): 
    #     if cnt == k  :  res, cnt = res+'-', 0  
    #     res, cnt , i = res+ letter[i], cnt+ 1, i +1   
    # return res 
    l = s.replace('-','').upper()[::-1]
    return '-'.join(l[i:i+k] for i in range(0, len(l), k))[::-1]

s = "2-5g-3-J"
k = 3
# s = "5F3Z-2e-9-w"
# k = 4
# s= '2'
# k = 2 
print(licenseKeyFormatting(s, k))