def sumEvenAfterQueries(nums, queries):
    """
    :type nums: List[int]
    :type queries: List[List[int]]
    :rtype: List[int]
    """
    res, sm = [], sum(n for n in nums if n%2 == 0 ) 
    for val , inx in queries: 
        prev, nums[inx] = nums[inx], nums[inx]+ val 
        if prev %2 == 0 : sm -= prev  
        if nums[inx] %2 == 0 :  sm+= nums[inx]

        res.append(sm)
    return res 


nums = [1,2,3,4]
queries = [[1,0],[-3,1],[-4,0],[2,3]]
print(sumEvenAfterQueries(nums, queries))