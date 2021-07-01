# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def search(nums, minval, maxval) :
    if minval == maxval : return TreeNode(val = nums[minval])
    elif minval < maxval : 
        midval = minval + (maxval-minval)//2 
        node = TreeNode(val= nums[midval])
        node.left = search( nums,minval, midval-1)
        node.right = search( nums,midval+1, maxval) 
        return node 


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        return search(nums, 0, len(nums)-1)