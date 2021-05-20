# Definition for singly-linked list:
class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None

def addTwoHugeNumbers(a, b):
    a = reverselinkedlist(a)
    b = reverselinkedlist(b)
    
    carry = 0
    result = None
    
    while a is not None or b is not None or carry > 0:
        raw = ((a.value if a is not None else 0) + 
               (b.value if b is not None else 0) + 
               carry)
                
        node = ListNode(raw % 10000)
        node.next = result
        
        result = node
        carry = raw // 10000
        
        if a is not None:
            a = a.next
        if b is not None:
            b = b.next
            
    return result
    
def reverselinkedlist(list):
    current = list
    previous = None
    
    while current is not None: 
        previous, current.next, current = current, previous, current.next
        
    return previous




def addTwoHugeNumbers(a, b):

    ar1 = []
    ar2 = []
    while a:
        ar1.append(a.value)
        a = a.next
    while b:
        ar2.append(b.value)
        b = b.next
    ar1 = ar1[::-1]
    ar2 = ar2[::-1]
    carry = 0
    res = []
    for i in range(max(len(ar1),len(ar2))):
        if i>=len(ar1) and i<len(ar2):
            x = carry + ar2[i]
        elif i>=len(ar2) and i<len(ar1):
            x = carry + ar1[i]
        elif i<len(ar1) and i<len(ar2):
            x = carry + ar1[i] + ar2[i]
        carry = x//10000
        x = x%10000
        res.append(x)
    if carry>0:
        res.append(carry)
    return res[::-1]