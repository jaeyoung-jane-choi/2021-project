
from collections import Counter 

def stringMatching(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    word= ' '.join(words) 
    return [w for w in words if word.count(w)> 1 ]

words = ["mass","as","hero","superhero"]
print(stringMatching(words))