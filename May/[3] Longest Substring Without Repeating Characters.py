
def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    
    if len(s) in [0,1] : return len(s)
    maxlen = 0
    for i in range(len(s)):
        d = {}
        while i<len(s) : 
            if s[i] in d : 
                break 
            else: 
                d[s[i]] = 1 
                i+=1 
        if len(d.keys()) > maxlen : maxlen = len(d.keys()) 
        
    return maxlen





    
s = "abcabcbb"
s = "pwwkew"
s = "bbbbb"
s='au'

print(lengthOfLongestSubstring(s))