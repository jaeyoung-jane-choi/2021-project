#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def isTreeSymmetric(t):
    def iTS(l,r):
        if not l and not r : return True 
        elif not l or not r : return False 
        else: 
            if l.value == r.value : return iTS(l.left, r.right) and iTS(l.right, r.left)
            else : return False 
    if not  t : return True 
    else: return iTS(t.left, t.right)