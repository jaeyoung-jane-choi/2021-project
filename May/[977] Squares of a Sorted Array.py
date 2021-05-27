class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i,j , res = 0, len(nums)-1 , []
        while i <= j : 
            if abs(nums[i]) < nums[j] : 
                res.append(nums[j]**2)
                j -=1 
            else : 
                res.append(nums[i]**2)
                i+=1 
                
        return res[::-1]