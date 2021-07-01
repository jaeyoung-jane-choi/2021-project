
#4 divide, not 100 but 400 -> 29(366)  /else  28 (365) 
def daysBetweenDates(date1, date2):
    """
    :type date1: str
    :type date2: str
    :rtype: int
    """
    def isLeap(year):
        return ((year%4==0) and (year%100!= 0)) or (year%400==0)

    def day(y,m,d) :
        #year calculation until current y 
        yd = 365* (y-1970)
        for year in range(1970,y): 
            if isLeap(year) : yd+=1
        
        month = [31,28,31,30,31,30,31,31,30,31,30,31]
        md = sum(month[:m-1])
        if isLeap(y) and m > 2 : md+=1
        return yd+md+d

    date1 ,date2= list(map(int, date1.split('-'))),list(map(int, date2.split('-')))

    return abs(day(*date1)- day(*date2))



date1 = "2019-06-29"
date2 = "2019-06-30"

# date1 = "2020-01-15"
# date2 = "2019-12-31"
print(daysBetweenDates(date1, date2))

