
from collections import defaultdict
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        d = defaultdict(int)
        curr,prev = head, head 
        while curr :
            if curr.val in d :
                prev.next = curr.next 
                curr = curr.next 
            else: 
                d[curr.val] == 1
                prev = curr 
                curr = curr.next 
                
        return head