
def fourSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    d= {}
    for i in range(len(nums)) : 
        for j in range(i+1, len(nums)) : 
            sums = nums[i] + nums[j]
            if sums in d: d[sums].append((i,j))
            else: d[sums] = [(i,j)]
    print(d)
    res =set()
    for key in d: 
        val= target - key 
        if val in d: 
            list1, list2 =d[key] , d[val]
            for (i,j) in list1:
                for (k,l) in list2: 
                    if i!=k and i!= l and j!=k and j!=l :  #중복으로 사용하니깐 
                        flist = sorted([nums[i],nums[j], nums[k], nums[l]])
                        res.add(tuple(flist))
                        
    return list(map(list , res))
                        





nums = [1,0,-1,0,-2,2]
target = 0



print(fourSum( nums, target))