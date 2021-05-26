
from collections import Counter 
def canConstruct(ransomNote, magazine):
    """
    :type ransomNote: str
    :type magazine: str
    :rtype: bool
    """
    print(Counter(ransomNote))
    print(Counter(magazine)
)
    return  not Counter(ransomNote)  - Counter(magazine) 


ransomNote = "ab"
magazine = "aab"
print(canConstruct(ransomNote, magazine))