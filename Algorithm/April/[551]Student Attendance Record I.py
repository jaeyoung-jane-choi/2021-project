

#A count < 2 
# L consecutive < 3 

from collections import Counter
def checkRecord(s):
    """
    :type s: str
    :rtype: bool
    """
    
    return s.count('A') < 2 and s.count('LLL') < 1 
    




    
s = 'PPALLP'
s = 'PPALLL'

print(checkRecord(s))