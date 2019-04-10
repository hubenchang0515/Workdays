# Workdays
A simple library about checking workdays and holidays

# Demo
```Python
from Workdays import *

# the normal work days
weekdays = [MON, TUE, WED, THU, FRI]

# special work days
workdays = [ 
    [2019,4,28], 
    [2019,5,5] 
]

# special holidays
holidays = [
    [2019, 5, 1],
    [2019, 5, 2],
    [2019, 5, 3],
    [2019, 5, 4]
]

# cout workdays and holidays
wd = Workdays(weekdays=weekdays, workdays=workdays, holidays=holidays)
print('Workdays of May is %d days' % wd.countWorkdays([2019,5,1], [2019,5,31]))
print('Holidays of May is %d days' % wd.countHolidays([2019,5,1], [2019,5,31]))
```

# Class
```Python
class Workdays(object) :

    # Constructor
    # Parameter
    #       weekdays : normal workdays
    #       workdays : special workdays
    #       holidays : special holidays
    def __init__(self, weekdays=[MON, TUE, WED, THU, FRI], workdays=[], holidays=[]):

    # Check if the day is a workday
    # Parameter
    #       day : day to check
    def isWorkday(self, day) :

    # Check if the day is a holiday
    # Parameter
    #       day : day to check
    def isHoliday(self, day) :

    # Count the workdays between the first and last
    # Parameter
    #       first : the first day (include)
    #       last  : the last day (include)
    def countWorkdays(self, first, last) :

    # Count the holidays between the first and last
    # Parameter
    #       first : the first day (include)
    #       last  : the last day (include)
    def countHolidays(self, first, last) :

    # Get the next workday after the day
    # Parameter
    #       day : after this day
    def nextWorkday(self, day) :

    # Get the previous workday before the day
    # Parameter
    #       day : before this day
    def prevWorkday(self, day) :

    # Get the next holiday after the day
    # Parameter
    #       day : after this day
    def nextHoliday(self, day) :

    # Get the previous holiday before the day
    # Parameter
    #       day : before this day
    def prevHoliday(self, day) :

    # Get the next week day after the day
    # Parameter
    #       day : after this day
    def nextWeekday(self, day, weekday) :

    # Get the previous week day before the day
    # Parameter
    #       day : before this day
    def prevWeekday(self, day, weekday) : 
```
