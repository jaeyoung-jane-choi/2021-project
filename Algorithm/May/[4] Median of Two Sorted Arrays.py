def findMedianSortedArrays( nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """

    res = []
    if len(nums1) == 0 : res = nums2
    elif len(nums2) == 0 : res = nums1 

    
    i=j=0
    while i < len(nums1) and j < len(nums2) : 
        if nums1[i] < nums2[j] : 
            res.append(nums1[i])
            i +=1 
        elif nums1[i]> nums2[j]:
            res.append(nums2[j])
            j+=1 
        else : 
            res.append(nums1[i])
            res.append(nums2[j])
            i, j = i+1, j+1 
        if i >= len(nums1) : 
            for jj in range(j, len(nums2)) : res.append(nums2[jj])
        if j >= len(nums2):
            for ii in range(i, len(nums1)) : res.append(nums1[ii])
    print(res)
    if len(res) %2 == 0 : return (res[len(res)//2] + res[(len(res)//2 )-1 ] ) / 2
    else: return  res[len(res)//2] 

nums1 = [1,2]
nums2 = [3,4]

nums1 = []
nums2 = [1]
print(findMedianSortedArrays( nums1, nums2))