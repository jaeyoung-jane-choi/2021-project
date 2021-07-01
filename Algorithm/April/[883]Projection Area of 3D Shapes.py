
def projectionArea(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    top= sum(element!=0 for i in grid for element in i )
    side= sum(max(i) for i in zip(*grid)) 
    front = sum(max(i[0]) for i in zip(grid)) 
    return top+front+side


grid =  [[1,2],[3,4]]
# grid = [[2]]
# grid= [[1,0],[0,2]]

print(projectionArea(grid))