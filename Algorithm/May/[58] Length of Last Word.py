
def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """
    s = s.strip(' ').split(' ')
    
    return len(s[-1])
    


s = "Hello World"
s= "a "
print(lengthOfLastWord(s))