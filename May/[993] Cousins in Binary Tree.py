# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        stack, res = [(root,0)], []
        if root.val in [x,y] : res.append((-1, 0))
        
        while stack : 
            popped, depth =stack.pop()
            if popped.right : 
                stack.append((popped.right,depth+1))
                if popped.right.val in [x,y] : res.append((popped.val,depth+1))
            if popped.left : 
                stack.append((popped.left,depth+1))
                if popped.left.val in [x,y] : res.append((popped.val,depth+1))
            
            if len(res) == 2 : break  
        
        return res[0][0]!= res[1][0] and res[0][1] == res[1][1] 