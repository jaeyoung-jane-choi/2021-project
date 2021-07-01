

from collections import deque
class RecentCounter(object):

    def __init__(self):
        self.request = deque()
        
    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.request.append(t)
        while self.request[0] < t-3000  : 
            self.request.popleft()
        return len(self.request)

       


obj = RecentCounter()
param_1 = obj.ping(1)
param_2= obj.ping(100)
print(param_1,param_2)

