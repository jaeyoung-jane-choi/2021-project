
def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    return sorted(s) == sorted(t)