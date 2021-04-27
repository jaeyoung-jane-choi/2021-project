
def arrayPairSum(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(sorted(nums)[::2])
        
nums = [1,4,3,2]
nums = [1,5,6,6,2,2]
print(arrayPairSum(nums))