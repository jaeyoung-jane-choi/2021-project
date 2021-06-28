def mergeAlternately(word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: str
    """  
    i, res = 0 , ''
    while i< max( len(word1) , len(word2))  : 
        if i < len(word1) : res+= word1[i]
        if i < len(word2) : res+= word2[i]
        i+=1 
    return res 

word1 = "abc"
word2 = "pqr"
print(mergeAlternately(word1, word2))
