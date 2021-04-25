from collections import defaultdict
def findJudge(N, trust):
    """
    :type N: int
    :type trust: List[List[int]]
    :rtype: int
    """
    count = [0] * (N+1)
    for i, j in trust:
        count[i] -= 1
        count[j] += 1
    for i in range(1,N+1): 
        if count[i] == N-1 : return i 
    return -1

    
N = 2
trust = [[1,2]]

N = 4 
trust  =[[1,3],[1,4],[2,3],[2,4],[4,3]]

N = 1
trust = []

# N= 3
# trust= [[1,3],[2,3],[3,1]]
print(findJudge(N, trust))