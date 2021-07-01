
def threeSumClosest(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    nums.sort()
    res = nums[0] + nums[1] + nums[2]
    for i in range(len(nums)-2) :
        j, k = i+1 , len(nums)-1 
        while j < k : 
            currsum = nums[i] + nums[j] + nums[k]
            if currsum == target : return currsum
            if abs(currsum-target) < abs(res-target) : res = currsum

            if currsum  < target : j+=1 
            elif currsum > target: k-=1 
    return res
    
nums = [-1,2,1,-4]
target = 1
print(threeSumClosest(nums, target))