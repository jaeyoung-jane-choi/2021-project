class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        jw, cnt = [l for l in jewels] , 0 
        for s in stones : 
            if s in jw : cnt+=1 
        return cnt
        # return sum(map(jewles.count, stones))