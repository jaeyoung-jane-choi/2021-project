class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res = []
        for i in range(left, right+1) : 
            flag =True  
            for j in str(i) : 
                if int(j) == 0 or i% int(j) != 0 : 
                    flag = False
                    break  
            if flag == True : res.append(i)
        print(res)
        return res