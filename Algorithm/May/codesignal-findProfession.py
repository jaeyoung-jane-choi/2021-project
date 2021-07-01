def findProfession(level, pos):
    # level 1 : E 
    # level 2: ED 
    # level 3 : EDDE 
    # level 4: EDDEDEED 
    bits = bin(pos-1).count('1')
    if bit %2 == 0 : return 'Engineer'
    else: 'Doctor'
    




level = 3
pos =3 
print( findProfession(level, pos))