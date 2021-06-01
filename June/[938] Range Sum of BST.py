# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
 
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        stack, res = [root], []
        while stack : 
            popped = stack.pop()
            if popped.val < high and popped.right :
                stack.append(popped.right)
            if popped.val > low and popped.left: 
                stack.append(popped.left)
            if low <= popped.val <= high : res.append(popped.val)
        return sum(res)