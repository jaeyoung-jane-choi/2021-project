 
import heapq

def largestSumAfterKNegations(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    
    # for i in range(k):
    #     minval = min(nums)
    #     for j in range(len(nums)) : 
    #         if nums[j] == minval : 
    #             nums[j] = -nums[j]
    #             break 
            
    # return sum(nums) 

    heapq.heapify(nums)
    for _ in range(k) : 
        heapq.heappush(nums, -heapq.heappop(nums))
    return sum(nums)
        

nums = [4,2,3]
k =1 

nums = [2,-3,-1,5,-4]
k = 2

nums = [5,6,9,-3,3]
k = 2
print(largestSumAfterKNegations(nums, k))