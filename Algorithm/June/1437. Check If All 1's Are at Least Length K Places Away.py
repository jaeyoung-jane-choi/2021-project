
def kLengthApart(nums, k):
    """
    :typae nums: List[int]
    :type k: int
    :rtype: bool
    """
    curr= float('inf')
    for i, n in enumerate(nums): 
        if n == 1 :
            if curr == float('inf'):   curr = i  
            else: 
                diff = i- curr -1  
                curr = i
                if diff < k : return False 
    return True 



nums = [1,0,0,0,1,0,0,1]
k = 2

nums = [1,0,0,1,0,1]
k = 2
print(kLengthApart( nums, k)) 