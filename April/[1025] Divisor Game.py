def divisorGame(n):
    """
    :type n: int
    :rtype: bool
    """
    cnt = 0 
    while n > 1 : 
        x =n-1
        if n % 2  == 0 : 
            while True : 
                if n%x ==0 and x%2 != 0 : break 
                x -=1 
            n, cnt = n-x, cnt+1 
            print('now n is..' , n)
        else : 
            n, cnt = n-1, cnt+1 
            print('now n is..' , n)

    return cnt%2!=0

    #easy solution 
    # return n % 2 == 0 

n = 3
print(divisorGame(n))