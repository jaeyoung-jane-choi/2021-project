
import enum


def findWords(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """ 
    d, res= {e: i  for i, ll in enumerate([list('qwertyuiop'),list('asdfghjkl'),list('zxcvbnm') ] ) for e in ll}, []
    for w in words : 
        row , flg =  d[w.lower()[0]] , True     
        for l in w.lower():  
            if row != d[l] :  
                flg = False 
                break 
        if flg : res.append(w)
    return res 



words = ["Hello","Alaska","Dad","Peace"]
print(findWords(words))