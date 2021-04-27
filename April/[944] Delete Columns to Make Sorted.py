def minDeletionSize(strs):
    """
    :type strs: List[str]
    :rtype: int
    """

    return sum([1 for s in zip(*strs) if ''.join(s) != ''.join(sorted(s))])




strs = ["cba","daf","ghi"]
strs = ['a','b']
# strs = ["zyx","wvu","tsr"]
print(minDeletionSize(strs))