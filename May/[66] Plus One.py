
def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    d = ''
    for n in digits: d+=str(n)
    return list( str(int(d) +1 ))


digits = [4,3,2,1]
print(plusOne(digits))