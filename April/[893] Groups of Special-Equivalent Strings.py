
def numSpecialEquivGroups(A):
    """
    :type A: List[str]
    :rtype: int
    """
    return len(set([''.join(sorted(a[::2]))+''.join(sorted(a[::1])) for a in A ]))
     
A= ["abcd","cdab","cbad","xyzz","zzxy","zzyx"]
print(numSpecialEquivGroups(A))
