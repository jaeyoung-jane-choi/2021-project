# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None : return 0 
        maxcnt = 0 
        stack = [(root,1)]
        while stack: 
            curr, depth = stack.pop()
            
            if curr.right : stack.append((curr.right, depth+1))
            if curr.left: stack.append((curr.left, depth+1))
            if depth > maxcnt : maxcnt= depth 
        return maxcnt 
            
            
            
            