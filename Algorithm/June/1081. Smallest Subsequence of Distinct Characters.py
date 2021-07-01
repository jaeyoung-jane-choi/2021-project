 
def smallestSubsequence(s):
    """
    :type s: str
    :rtype: str
    """
    lst, stack = {c:i for i, c in enumerate(s)}, []
    for i, c in enumerate(s):
        if c in stack : continue
        while stack and stack[-1] > c and i< lst[stack[-1]] : stack.pop()
        stack.append(c)

    return ''.join(stack)

s = "bcabc"
print(smallestSubsequence(s))