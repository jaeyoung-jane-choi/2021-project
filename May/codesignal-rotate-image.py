def rotateImage(a):

    n = len(a)
     
     
    # #1 transpose 
    # for i in range(n): 
    #     for j in range(i+1, n):
    #         tmp = a[i][j]
    #         a[i][j], a[j][i] = a[j][i], tmp 
    
    # #2 flip 
    # for i in range(n) : 
    #     for j in range(n//2):
    #         tmp = a[i][j]
    #         a[i][j], a[i][n-j-1]   = a[i][n-j-1]  , tmp 
            
    # return a 
    a.reverse()
    
    for i in range(n) : 
        for j in range(i+1,n): 
            tmp = a[i][j] 
            a[i][j] , a[j][i] = a[j][i] , tmp 
    return a 