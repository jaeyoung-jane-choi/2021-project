

def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    if len(nums) < 3  :return []
    n,p,z = [], [], []
    res = set()
    for num in nums : 
        if num > 0 : p.append(num)
        elif num < 0 : n.append(num)
        else: z.append(num)

    N,P = set(n), set(p)

    #(-3, 0, 3)
    if z : 
        for num in P : 
            if -1*num in N : res.add((-1*num, 0, num))

    # (0,0,0)
    if len(z) >= 3 : res.add((0,0,0))

    # (-1, -2 ,3 )
    for i in range(len(n)) : 
        for j in range(i+1, len(n)) :
            target = -1 * (n[i] + n[j])
            if target in P : res.add(tuple(sorted([n[i], n[j],target])))

    #(-4,1,3)
    for i in range(len(p)):
        for j in range(i+1, len(p)): 
            target = -1*(p[i]+p[j])
            if target in N : res.add(tuple(sorted([p[i], p[j],target])))

    
    return list(map(list, res) )

nums = [-1,0,1,2,-1,-4]
print(threeSum( nums))