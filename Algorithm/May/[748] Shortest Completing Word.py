import re 
from collections import Counter 

def shortestCompletingWord(licensePlate, words):
    """
    :type licensePlate: str
    :type words: List[str]
    :rtype: str
    """
    d = Counter(re.sub('\d|\W','',licensePlate).lower())  
    

    res = [w for w in words if d-Counter(w) == Counter() ]
    return sorted(res, key = lambda x : len(x))[0]



licensePlate = "1s3 PSt"
words = ["step","steps","stripe","stepple"]
licensePlate = "1s3 456"
words = ["looks","pest","stew","show"]
print(shortestCompletingWord(licensePlate, words)) 