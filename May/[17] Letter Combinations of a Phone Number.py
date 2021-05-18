from itertools import combinations

def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    if len(digits) == 0 : return []
    dic = {2: 'abc', 3 :'def', 4: 'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'}

    res = ['']
    for num in digits :
        tmp = []
        for a in res :
            for k in dic[int(num)] : tmp.append(a+k)
        res = tmp 
    return res 
    

digits = "23"

print(letterCombinations(digits))
