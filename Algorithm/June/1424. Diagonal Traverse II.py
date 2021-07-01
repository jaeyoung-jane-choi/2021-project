
import collections


def findDiagonalOrder(nums):
    """
    :type nums: List[List[int]]
    :rtype: List[int]
    """
    res, n, queue = [], len(nums), collections.deque([(0,0)])
    while queue : 
        row, col = queue.popleft()
        res.append(nums[row][col])
        if col == 0 and row +1 < n : queue.append((row+1, col))
        if col+1 < len(nums[row]) : queue.append((row,col+1))
    return res 
nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
# nums = [[1,2,3],[4,5,6],[7,8,9]]
print(findDiagonalOrder(nums))