# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        
        stack, res = [(root,0) ] , {}
        while stack: 
            node, level = stack.pop()
            if node.right : stack.append((node.right,level+1))
            if node.left : stack.append((node.left,level+1))
                
            if level in res :  res[level][0], res[level][1]= res[level][0]+node.val, res[level][1]+1 
            else : res[level] = [node.val, 1] 
            
        print(res.items())
        return [ float(v[0]) / float(v[1])  for k, v in sorted(res.items())]
            