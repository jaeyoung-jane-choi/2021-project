# Singly-linked lists are already defined with this interface:
class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None

def removeKFromList(l, k):
    head =prev = ListNode(0)
    head.next = l
    curr = head.next 
    while curr :
        if curr.value == k : 
            prev.next = curr.next 
            curr = curr.next 
        else: 
            prev =curr 
            curr =curr.next 
    return head.next 


def removeKFromList(l, k):
    c = l
    while c:
        if c.next and c.next.value == k:
            c.next = c.next.next
        else:
            c = c.next
    return l.next if l and l.value == k else l