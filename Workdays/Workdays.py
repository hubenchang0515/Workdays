#! /usr/bin/env python3
import datetime

# constant of week days
MON = datetime.datetime(2019, 4, 1).weekday()
TUE = datetime.datetime(2019, 4, 2).weekday()
WED = datetime.datetime(2019, 4, 3).weekday()
THU = datetime.datetime(2019, 4, 4).weekday()
FRI = datetime.datetime(2019, 4, 5).weekday()
SAT = datetime.datetime(2019, 4, 6).weekday()
SUN = datetime.datetime(2019, 4, 7).weekday()

class Workdays(object) :
    def __init__(self, weekdays=[MON, TUE, WED, THU, FRI], workdays=[], holidays=[]):
        self.weekdays = weekdays
        
        self.workdays = []
        for day in workdays :
            self.workdays.append(self.date(day))
        self.workdays = set(self.workdays)
            
        self.holidays = []
        for day in holidays :
            self.holidays.append(self.date(day))
        self.holidays = set(self.holidays)
        
        error_days = self.workdays & self.holidays
        if len(error_days) > 0 :
            raise Exception(error_days)
        
    def date(self, day) :
        if isinstance(day, datetime.datetime) :
            _day = day.date()
        elif isinstance(day, datetime.date) :
            _day = day
        elif isinstance(day, list) and len(day) == 3 : 
            _day = datetime.date(day[0], day[1], day[2])
        elif isinstance(day, tuple) and len(day) == 3 : 
            _day = datetime.date(day[0], day[1], day[2])
        else :
            raise Exception("Invalid date parameter")
        
        return _day
        
    def isWorkday(self, day) :
        _day = self.date(day)
        if _day in self.holidays :
            return False
        elif _day.weekday() in self.weekdays :
            return True
        elif _day in self.workdays :
            return True
        else :
            return False
            
    def isHoliday(self, day) :
        return not self.isWorkday(day)
        
    def countWorkdays(self, first, last) :
        _first = self.date(first)
        _last  = self.date(last)
        assert _first <= _last
        current = _first
        count = 0
        while current <= _last :
            if self.isWorkday(current) :
                count = count + 1
            current = current + datetime.timedelta(days=1)
            
        return count
        
    def countHolidays(self, first, last) :
        _first = self.date(first)
        _last  = self.date(last)
        assert _first <= _last
        current = _first
        count = 0
        while current <= _last :
            if self.isHoliday(current) :
                count = count + 1
            current = current + datetime.timedelta(days=1)
            
        return count
        
    def nextWorkday(self, day) :
        _day = self.date(day)
        current = _day + datetime.timedelta(days=1)
        while not self.isWorkday(current) :
            current = current + datetime.timedelta(days=1)
            
        return current
        
    def prevWorkday(self, day) :
        _day = self.date(day)
        current = _day - datetime.timedelta(days=1)
        while not self.isWorkday(current) :
            current = current - datetime.timedelta(days=1)
            
        return current
        
        
    def nextHoliday(self, day) :
        _day = self.date(day)
        current = _day + datetime.timedelta(days=1)
        while not self.isHoliday(current) :
            current = current + datetime.timedelta(days=1)
            
        return current
        
    def prevHoliday(self, day) :
        _day = self.date(day)
        current = _day - datetime.timedelta(days=1)
        while not self.isHoliday(current) :
            current = current - datetime.timedelta(days=1)
            
        return current
        
    def nextWeekday(self, day, weekday) :
        _day = self.date(day)
        current = _day + datetime.timedelta(days=1)
        while not current.weekday() == weekday :
            current = current + datetime.timedelta(days=1)
            
        return current
            
    def prevWeekday(self, day, weekday) :
        _day = self.date(day)
        current = _day - datetime.timedelta(days=1)
        while not current.weekday() == weekday :
            current = current - datetime.timedelta(days=1)
        
        return current
if __name__ == '__main__' :
    workdays = Workdays(holidays=[datetime.date(2019, 4, 5)])
    print(workdays.countWorkdays([2019, 1, 1], [2019,12,31]))
    print(workdays.countHolidays([2019, 1, 1], [2019,12,31]))