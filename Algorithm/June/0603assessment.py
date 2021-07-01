class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 : return False 
        return str(x) == str(x)[::-1]


class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        i , j , r , res = len(num1)-1 , len(num2)-1, 0 , ''
        while i >= 0 or j >= 0 : 
            n = int(num1[i]) + int(num2[j]) + r 
            if n >= 10 : r, n = n//10 , n%10 
            else: r = 0 
            res, i, j= res+ str(n) , i-1, j-1  
            if i < 0 : 
                while j >= 0 :
                    n = int(num2[j]) + r  
                    if n >= 10 : r, n = n//10 , n%10 
                    else: r = 0  
                    res , j = res+ str(n) , j-1 
            elif j < 0 : 
                while i >= 0 :
                    n = int(num1[i]) + r  
                    if n >= 10 : r, n = n//10 , n%10 
                    else: r = 0  
                    res , i = res+ str(n) , i-1  
        if r != 0  : res+= str(r)
        return res[::-1]