# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # if not root : return []
        # stack, res, visited = [root] , [] , []
        # while stack : 
        #     popped = stack.pop()
        #     if popped in visited: res.append(popped.val)
        #     else:
        #         if popped.right and popped.left: 
        #             visited.append(popped)
        #             stack.append(popped)
        #             stack.append(popped.right)
        #             stack.append(popped.left)
        #         elif popped.left: 
        #             visited.append(popped)
        #             stack.append(popped)
        #             stack.append(popped.left) 
        #         elif popped.right: 
        #             visited.append(popped)
        #             stack.append(popped)
        #             stack.append(popped.right)
                    
        #         else: res.append(popped.val)
                
        # return res 
        res , stack = [], [(root, False)]
        while stack : 
            node, visited = stack.pop()
            if node : 
                if visited : res.append(node.val)
                else:
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False ))
        return res 