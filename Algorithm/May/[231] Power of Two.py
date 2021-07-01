class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1 : return True
        if n <= 0 : return False  
        while n > 1  : 
            m,r = divmod(n,2)
            if m == 1 and r == 0 : return True 
            if r == 1 or m%2 != 0 :return False 
            n = m 
        return True 
            
            