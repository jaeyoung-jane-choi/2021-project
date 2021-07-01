# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack, maxcnt = [root] , 0 
        while stack : 
            popped = stack.pop()
            if popped.right : stack.append(popped.right)
            if popped.left : stack.append(popped.left)
        
            if popped.left and popped.right : cnt= self.length(popped.left) + self.length(popped.right)
            elif popped.left : cnt = self.length(popped.left)
            elif popped.right : cnt = self.length(popped.right)
            else: cnt = 0 
            if cnt > maxcnt : maxcnt = cnt 
                
            
        return maxcnt 
    
    def length(self, t) :
        if not t : return 0
        
        stack, maxcnt = [(t,1)] , 0
        while stack: 
            popped,cnt = stack.pop()
            if popped.right : stack.append((popped.right,cnt+1))
            if popped.left : stack.append((popped.left,cnt+1))
            if cnt > maxcnt : maxcnt = cnt 
                
        return maxcnt 



class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.ans = 0 

        def depth(p) :
            if not p : return 0 
            left, right = depth(p.left), depth(p.right)
            self.ans = max(self.anx, left+right)
            return 1+ max(left, right)
        
        depth(root)
        return self.ans