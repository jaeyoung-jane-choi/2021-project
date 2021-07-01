# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def middleNode(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """ 
    prev = curr = head
     while curr and curr.next:
        prev = prev.next
        curr = curr.next.next
    
    return prev 