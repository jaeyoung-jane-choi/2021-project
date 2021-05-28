# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        stack = [root]
        while stack :
            popped = stack.pop()
            if popped: 
                popped.right , popped.left = popped.left, popped.right 
                stack.append(popped.right)
                stack.append(popped.left)
        return root 