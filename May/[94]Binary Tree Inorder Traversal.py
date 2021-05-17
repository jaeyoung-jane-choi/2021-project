# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack, res, visited = [root], [] , []
        if root == None : return []
        while stack: 
            curr = stack.pop()
            if curr in visited: res.append(curr.val)
            else: 
                if curr.right : stack.append(curr.right)
                if curr.left: 
                    stack.append(curr)
                    stack.append(curr.left)
                    visited.append(curr)
                else : res.append(curr.val)

        return res 