 
def nextGreatestLetter(letters, target):
    """
    :type letters: List[str]
    :type target: str
    :rtype: str
    """
    for l in letters: 
        if l > target : return l 
    return letters[0]

letters = ["c","f","j"]
target = "j"
print(nextGreatestLetter(letters, target))