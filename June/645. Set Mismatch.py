from collections import Counter 

def findErrorNums(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """ 
    # res= [Counter(nums).most_common(1)[0][0]]
    # for n in range(1, len(nums)+1) : 
    #     if n not in nums : res.append(n)
    # return res 
    return [sum(nums) - sum(set(nums)), sum(range(1, len(nums)+1)) - sum(set(nums))] 

nums = [1,2,2,4]
# nums =[1,1]
print(findErrorNums(nums))