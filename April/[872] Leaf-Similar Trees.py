# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def leafSimilar(root1, root2):
    """
    :type root1: TreeNode
    :type root2: TreeNode
    :rtype: bool
    """
    return lastleaf(root1) == lastleaf(root2)

    

#simple version 
def lastleaf(root):
    if not root: return []
    if not (root.left or root.right ) : return [root.val]
    return lastleaf(root.left) + lastleaf(root.right)


#use stack 
def lastleafstack(root,s):
    if root is not None: 
        stack = []
        stack.append(root)
        while stack: 
            x = stack.pop(-1)
            if x.left is None and x.right is None: 
                s.append(x.val)
                continue
            if x.right is not None: stack.append(x.right)
            if x.left is not None: stack.append(x.left)
    return s 

root1 = [3,5,1,6,2,9,8,None,None,7,4]
root2 = [3,5,1,6,7,4,2,None,None,None,None,None,9,8]

# leafSimilar(root1,root2)
print(lastleaf(root1,0))