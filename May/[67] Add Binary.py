
def addBinary(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    return  bin(int(a,2) + int(b,2))[2:]

    

a = "11"
b = "1"
print(addBinary(a, b))