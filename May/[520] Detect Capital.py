def detectCapitalUse(word):
    """
    :type word: str
    :rtype: bool
    """
    if word == word.upper() : return True 
    elif word == word.lower() : return True 
    elif word[0] == word[0].upper() and word[1:] == word[1:].lower() : return True 
    return False 

    # return word.isupper() or word.islower() or word.istitle()
    
word ='USA'
word = 'FooT'
print(detectCapitalUse(word))