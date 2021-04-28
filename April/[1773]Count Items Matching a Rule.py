def countMatches(items, ruleKey, ruleValue):
    """
    :type items: List[List[str]]
    :type ruleKey: str
    :type ruleValue: str
    :rtype: int
    """
    d = {'type':0,'color':1,'name':2}
    return sum(1 for i in items if i[d[ruleKey]] == ruleValue  )





items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
ruleKey = "color"
ruleValue = "silver"


items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]]
ruleKey = "type"
ruleValue = "phone"
print(countMatches(items, ruleKey, ruleValue))