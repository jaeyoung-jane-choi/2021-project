# Singly-linked lists are already defined with this interface:
class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None

def mergeTwoLinkedLists(l1, l2):
    l1curr, l2curr, l = l1, l2 , ListNode(0)
    lcurr = l 
    while l1curr or l2curr :
        if not l1curr : 
            while l2curr: 
              lcurr.next= l2curr
              l2curr, lcurr = l2curr.next , lcurr.next 
            break 
              
        elif not l2curr : 
            while l1curr: 
              lcurr.next= l1curr
              l1curr, lcurr = l1curr.next , lcurr.next
            break 
              
        else:      
            if l1curr.value > l2curr.value : 
                lcurr.next= l2curr
                l2curr, lcurr = l2curr.next , lcurr.next 
            elif l1curr.value < l2curr.value: 
                lcurr.next= l1curr
                l1curr, lcurr= l1curr.next , lcurr.next
            else:
                lcurr.next= l1curr
                l1curr, lcurr = l1curr.next , lcurr.next
                lcurr.next= l2curr
                l2curr, lcurr = l2curr.next , lcurr.next 

    return l.next 
