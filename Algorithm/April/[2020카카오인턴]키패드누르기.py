
def diff(l,nums): 
    if l in [1,4,7,10] : #left 
        return sum( abs(i-j) for i,j in zip( ((((l-2)//3)+1), -1 ) , divmod(nums-2,3) )) 
    return sum( abs(i-j) for i,j in zip(divmod(l-2,3), divmod(nums-2,3) ) )

def solution(numbers, hand):
    answer, n = '', 0 
    d = {'*' :10 , 0: 11, '#':12}
    l, r = d['*'] , d['#']
    while n < len(numbers) : 
        nums = d[numbers[n]] if numbers[n] in d else numbers[n]
        print('the num is..'+str(nums))        
    
        if (nums-2)%3 == 1 : 
            print('right' , nums)
            r = nums
            answer+='R'
        elif (nums-2)%3 == 2 : 
            print('left' , nums)
            l = nums
            answer+='L'
        else: 
            print('left' , str(l))
            print('right' , str(r))
            if l in d: l = d[l]
            if r in d: r = d[r]
            lm =  diff(l,nums)
            lr = diff(r,nums)
            print('each level difference is..', lm, lr )

            if lm < lr :
                print('left is closer')
                l = numbers[n]
                answer+='L'
            elif lm > lr : 
                print('right is closer')
                r = numbers[n]
                answer+='R'
            else: 
                print('same so ', hand)
                if hand == 'left' :
                    l = numbers[n]
                    answer+='L'
                else: 
                    r = numbers[n]
                    answer+='R'

        n+=1 
    return answer

#easier : just create location's position 
# key_dict = {1:(0,0),2:(0,1),3:(0,2),
                # 4:(1,0),5:(1,1),6:(1,2),
                # 7:(2,0),8:(2,1),9:(2,2),
                # '*':(3,0),0:(3,1),'#':(3,2)}

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = 'right'

numbers =  [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = 'left'

numbers =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
hand ='right'

print(solution(numbers, hand) == 'LLRLLRLLRL')