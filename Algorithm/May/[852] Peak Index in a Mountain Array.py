class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        s, l, peak = 0, len(arr)-1 , 0 
        while s<= l : 
            mid = s+ (l-s)//2 
            if arr[mid-1] < arr[mid] > arr[mid+1] : 
                peak = mid 
                break 
            elif arr[mid-1] < arr[mid]  < arr[mid+1]: 
                s = mid +1 
            else : l = mid -1 
        return peak 
            