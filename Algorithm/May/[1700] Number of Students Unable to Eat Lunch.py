from collections import Counter

def countStudents(students, sandwiches):
    """
    :type students: List[int]
    :type sandwiches: List[int]
    :rtype: int
    """
    c= Counter(students)
    for s in sandwiches:
        if c[s] == 0 : break 
        c[s]-=1 
    return c[0] + c[1]


students = [1,1,1,0,0,1]
sandwiches = [1,0,0,0,1,1]
print(countStudents(students, sandwiches))