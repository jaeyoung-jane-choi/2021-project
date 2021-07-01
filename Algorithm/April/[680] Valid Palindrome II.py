def validPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    i,j =  0, len(s)-1 
    while i < j :
        if s[i] != s[j]: 
            first , second = s[i:j], s[i+1:j+1]
            return first == first[::-1] or second == second[::-1]
        i, j = i+1, j-1 
    return True 






# s='abcddba'
# s= 'abca'
s= 'abac'
s = 'eeccccbebaeeabebccceea'
s = "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"

print(validPalindrome(s))