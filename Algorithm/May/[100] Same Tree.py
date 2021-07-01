# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        stack = [(p,q)]
        while stack : 
            n1, n2 = stack.pop()
            if n1 and n2 and n1.val == n2.val : 
                stack.append((n1.right, n2.right))
                stack.append((n1.left, n2.left))
            elif not n1 and not n2: continue 
            else : return False 
        return True 