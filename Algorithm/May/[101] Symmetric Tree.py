# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack = [(root.left, root.right)]
        while stack: 
            l, r = stack.pop()
            if l and r and l.val == r.val : 
                stack.append((l.left, r.right))
                stack.append((l.right, r.left))
            elif not l and not r : continue
            else : return False 
        return True 