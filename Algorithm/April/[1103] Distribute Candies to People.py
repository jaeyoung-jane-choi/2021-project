def distributeCandies(candies, num_people):
    """
    :type candies: int
    :type num_people: int
    :rtype: List[int]
    """
    res = [0] * num_people
    i, j = 1 , 0 
    while candies!= 0 : 
        print(res)
        if j > len(res)-1: 
            print(' j is now again 0')
            j = 0 

        if candies - i < 0 : 
            print(j)
            print('cant substract '+ str(i))
            print('candies is currently'+ str(candies))
            res[j]+=candies
            break

        res[j] += i 
        candies= candies- i 

        j+=1 
        i+=1
    return res 

        

candies = 7
num_people = 4
candies = 10
num_people = 3
print(distributeCandies(candies, num_people))