
def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    return haystack.find(needle)


haystack = "hello"
needle = "ll"

haystack = ""
needle = ""
print(strStr(haystack, needle))