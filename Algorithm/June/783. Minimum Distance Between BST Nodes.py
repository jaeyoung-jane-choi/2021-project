# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack, res = [root], []
        while stack : 
            pop = stack.pop()
            if pop.right : stack.append(pop.right)
            if pop.left : stack.append(pop.left)
            res.append(pop.val)
        res.sort()
        val = float('inf')
        for i, j in zip(res, res[1:]): 
            if val > j-i : val = j-i
        return val