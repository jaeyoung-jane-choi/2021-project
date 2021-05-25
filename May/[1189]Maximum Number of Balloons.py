def maxNumberOfBalloons(text):
    """
    :type text: str
    :rtype: int
    """ 
    #b : 1 a: 1 l: 2 o : 2 n :1  
    return min(text.count('b'), text.count('a'), text.count('l')//2 , text.count('o')//2 , text.count('n'))
text=  "nlaebolko"
# text = 'loonbalxballpoon'
print(maxNumberOfBalloons(text))