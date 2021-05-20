# Definition for singly-linked list:
class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None

def isListPalindrome(l):
    if not l or not l.next: return True
    n, t = l , []
    while n :
        t.append(n.value)
        n = n.next 
    return t == t[::-1]
    