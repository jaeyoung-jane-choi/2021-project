def secondHighest(s):
    """
    :type s: str
    :rtype: int
    """

    try : return sorted(set([int(i) for i in s if i.isdigit() ]))[-2]
    except: return -1 


s = "dfa12321afd"
# s = 'ad'
print( secondHighest(s))