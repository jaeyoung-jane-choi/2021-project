class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None


def reverseNodesInKGroups(l,k):
    curr = l 
    for _ in range(k) : 
        if not curr : return l
        curr = curr.next 
    
    res, curr  = l, l.next 
    for _ in range(k-1) : 
        curr.next , curr , res = res, curr.next , curr
    l.next = reverseNodesInKGroups(curr, k)
    return res 

def reverseNodesInKGroups(l,k):
    if not l : return l 
    c , n = l, k 
    while c and n : 
        c = c.next 
        n -= 1 
    if n : return l 

    curr, prev, nex , n  = l, None, None , k 
    while curr and n : 
        nex = curr.next 
        curr.next = prev 
        prev = curr 
        curr = next 
        n -=1 
    if nex : l.next = reverseNodesInKGroups(next, k)
    return prev