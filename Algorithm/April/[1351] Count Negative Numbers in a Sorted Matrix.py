def countNegatives(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    l,r, n, m = [],[],0, 0 
    while  m < len(grid) :
        while n < len(grid[0]) and n not in l: 
            if grid[m][n] < 0 :  
                print('dont need to go farther than ' +str(n))
                l.append(n) 
                r.append(m) 
                print(grid[m][n])        
            n +=1 
        m +=1 
        n =0 
    return sum([len(grid)-i for i in r ])
        
grid =  [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
grid = [[1,-2],[-3,-4]]
grid = [[3,2],[1,0]]
grid = [[-1]]
print(countNegatives(grid))