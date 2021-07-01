# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def rearrangeLastN(l, n):
    if not l or n==0 : return l 
    slow = fast =l 
    
    for _ in range(n) :  fast = fast.next 

    if slow == fast or not fast : return l  
    while fast.next :  slow, fast = slow.next, fast.next      
    k = n 
    while k : 
        tmp = slow.next 
        slow.next = tmp.next 
        if k != n : 
            tmp.next = curr.next 
            curr.next = tmp 
            curr = curr.next 
        else : 
            tmp.next = l
            l = curr = tmp   
            
        k -=1 
    
    return l 



def rearrangeLastN(l, n):
    if n == 0: return l
    front, back = l, l
    for _ in range(n): front = front.next
    if not front: return l

    while front.next:
        front , back = front.next , back.next
    out = back.next
    back.next = None
    front.next = l
    return out
    

