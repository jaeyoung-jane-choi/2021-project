
import collections


def intersect(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """ 
    a, b = map(collections.Counter, (nums1, nums2)) 
    return list((a&b).elements())
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

nums1= [1,2,2,1]
nums2= [2,2]
print(intersect(nums1,nums2))