
def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    if numRows == 1 or numRows >= len(s): return s

    n= [''] * numRows
    indx = 0
    for x in s :
        n[indx] += x 
        if indx == 0 : step= 1 
        elif indx == numRows-1 : step= -1 
        indx += step 
         
    return ''.join(n)

s = "PAYPALISHIRING"
numRows = 3
print(convert(s, numRows))