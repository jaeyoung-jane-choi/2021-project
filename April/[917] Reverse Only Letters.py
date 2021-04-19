def reverseOnlyLetters(S):
    """
    :type S: str
    :rtype: str
    """

    #using while loop 
    # i, j = 0, len(S)-1
    # S= list(S)
    # while i < j : 
    #     while i<j and not S[i].isalpha() : i+=1 
    #     while i< j and not S[j].isalpha() : j-=1 
    #     S[i], S[j] = S[j], S[i]
    #     i, j = i+1 , j-1 
    # return ''.join(S)

    stack = [s for s in S if s.isalpha()]
    return ''.join( stack.pop() if s.isalpha() else s for s in S)

S =  "Test1ng-Leet=code-Q!"
# S= "a-bC-dEf-ghIj"
print(reverseOnlyLetters(S))
