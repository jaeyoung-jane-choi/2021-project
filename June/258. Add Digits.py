def addDigits(num):
    """
    :type num: int
    :rtype: int
    """
    while num / 10 >= 1 :  num = sum( int(n) for n in str(num) )
    return num

num = 38 
print(addDigits(num))