# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root : return []
        res,q ={}, deque([(0,root)])
        while q:
            level, popped = q.popleft()
            if popped.left : q.append((level+1, popped.left))
            if popped.right: q.append((level+1, popped.right))
            if level not in res : res[level] = popped.val
            else: res[level] = popped.val
        return [j for i,j in sorted(res.items(), key= lambda x : x[0])]

