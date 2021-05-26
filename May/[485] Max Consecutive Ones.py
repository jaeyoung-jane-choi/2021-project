class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i= length = maxlength = 0 
        while i < len(nums): 
            if nums[i] == 1: length, i = length +1 , i +1  
            else :  length, i  = 0  , i +1
                
            maxlength = max(maxlength, length)
        return maxlength 