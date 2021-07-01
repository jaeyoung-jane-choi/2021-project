
def flipAndInvertImage(image):
    """
    :type image: List[List[int]]
    :rtype: List[List[int]]
    """
    return [[1^i for i in reversed(row) ] for row in image]
        
    

image =image = [[1,1,0],[1,0,1],[0,0,0]]
print(flipAndInvertImage(image))