#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def hasPathWithGivenSum(t, s):
    # if t is None : return s == 0 
    # return hasPathWithGivenSum(t.left, s-t.value) or hasPathWithGivenSum(t.right, s-t.value)

    if not t: return s ==0 
    
    s = s-t.value 
    if not t.left and not t.right : return s== 0 
    elif t.left and t.right : return hasPathWithGivenSum(t.left, s) or hasPathWithGivenSum(t.right,s)
    elif t.left and not t.right : return hasPathWithGivenSum(t.left, s)
    elif not t.left and t.right : hasPathWithGivenSum(t.right, s)

        