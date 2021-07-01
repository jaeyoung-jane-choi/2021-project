# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if not head or not head.next: return head
        
        dummy = prev = ListNode(0)
        prev.next = head
		
        while prev.next and prev.next.next:
            a = prev.next
            b = prev.next.next
            c = prev.next.next.next
            prev.next = b
            prev.next.next = a
            prev.next.next.next = c
            prev = prev.next.next
        return dummy.next