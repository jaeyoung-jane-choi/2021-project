class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        # self.nums = nums  
        self.acc = [0, *itertools.accumulate(nums)]

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        
        # return sum(self.nums[left:right+1])
        return self.acc[right+1] - self.acc[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)