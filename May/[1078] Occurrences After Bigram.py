


def findOcurrences(text, first, second):
    """
    :type text: str
    :type first: str
    :type second: str
    :rtype: List[str]
    """
    t, res = text.split(' '), []
    for i in range(len(t)-2 ):
        if t[i] == first and t[i+1] == second : res.append(t[i+2])
    return res 
        
        
    
text = "alice is a good girl she is a good student" 
first = "a"
second = "good"

text = "we will we will rock you"
first = "we"
second = "will"
print(findOcurrences(text, first, second))