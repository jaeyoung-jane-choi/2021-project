import re 
def numDifferentIntegers(word):
    """
    :type word: str
    :rtype: int
    """
    word = re.sub(r'\D', ' ', word).strip(' ')
    word = re.sub(r'\s+', ' ', word).split(' ') 

    if word[0] == '': return 0 

    res = set() 
    for w in word :  
        if int(w) not in res : res.add(int(w)) 
    return len(res)


word = "a123bc34d8ef34"
word =  "a1b01c001"
word = 'ab'
print(numDifferentIntegers(word))