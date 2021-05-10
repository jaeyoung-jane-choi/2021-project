class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k -1 
        self.nums = sorted(nums, reverse=True )  
        

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        self.nums.append(val) 
        self.nums= sorted(self.nums,reverse= True)
        return self.nums[self.k]
        


#using heapq 
import heapq
class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.heap = nums
        heapq.heapify(self.heap)
        self.k = k

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        heapq.heappush(self.heap,val)
        # if heap grows bigger then k remove elements
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)