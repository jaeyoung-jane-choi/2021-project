 
from collections import deque
def sequentialDigits(low, high):
    """
    :type low: int
    :type high: int
    :rtype: List[int]
    """ 
    res = []
    q = deque(range(1,10)) 
    while q : 
        num = q.popleft()
        if low <= num <= high: res.append(num)
        rem = num % 10  
        if rem != 9 : q.append(num *10 + rem+1)
    return res 

low = 100
high = 300
print(sequentialDigits(low, high)) 