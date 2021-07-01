"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res, stack = [], [root]
        if root == None : return res 
        while stack : 
            curr = stack.pop()
            res.append(curr.val)
            stack.extend(curr.children)
        return res[::-1]