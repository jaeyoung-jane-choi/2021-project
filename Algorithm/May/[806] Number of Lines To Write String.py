
def numberOfLines(widths, s):
    """
    :type widths: List[int]
    :type s: str
    :rtype: List[int]
    """
    alphabet, dic = "abcdefghijklmnopqrstuvwxyz", {}
    for i , l in enumerate(alphabet): dic[l] = i
    
    tot, cnt = 0, 1 
    for letter in s: 
        if widths[dic[letter]] + tot > 100 :  cnt, tot =cnt+1, widths[dic[letter]] 
        else: tot += widths[dic[letter]] 


    return [cnt,tot]


widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
s = "abcdefghijklmnopqrstuvwxyz"

# widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
# s = "bbbcccdddaaa"
print(numberOfLines(widths, s))