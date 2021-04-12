from collections import Counter
def uncommonFromSentences(A, B):
    """
    :type A: str
    :type B: str
    :rtype: List[str]
    """
    
    c = Counter(A.split()+ B.split())
    return [item for item in c if c[item] < 2 ]

A = "this apple is sweet"
B = "this apple is sour"


A = "apple apple" 
B = "banana"
print(uncommonFromSentences(A, B))
