#You are given the following information, but you may prefer to do some research for yourself.

#1 Jan 1900 was a Monday. 
#Thirty days has September,
#April, June and November.
#All the rest have thirty-one,
#Saving February alone,
#Which has twenty-eight, rain or shine.
#And on leap years, twenty-nine. 
#A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400. 
#How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

def isLeap(year):
    if (year % 100) == 0:
        if (year % 400): return True
        else: return False
    if ((year % 4) == 0): return True
    return False

class dayState:
    def __init__(self, day="Sun"):
        self.day=day
        return None
    
    def nextDay(self):
        if self.day=="Sun": self.day="Mon"
        else:
            if self.day=="Mon": self.day="Tue"
            else:
                if self.day=="Tue": self.day="Wed"
                else:
                    if self.day=="Wed": self.day="Thu"
                    else:
                        if self.day=="Thu": self.day="Fri"
                        else:
                            if self.day=="Fri": self.day="Sat"
                            else: self.day="Sun"
        return self.day
    

leap_months=[31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
norm_months=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

a=dayState()

numberOfSundays=0
for month in norm_months:
    for days in range(1, month+1):
        a.nextDay()




for year in range(1901, 2001):
    if isLeap(year): thisYear=leap_months
    else: thisYear=norm_months
    for month in thisYear:
        for days in range(1, month+1):
            if a.nextDay() == "Sun" and days==1:
                numberOfSundays=numberOfSundays + 1

print numberOfSundays


            
        
        
