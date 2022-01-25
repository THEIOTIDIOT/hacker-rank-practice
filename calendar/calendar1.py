# https://docs.python.org/2/library/calendar.html#calendar.setfirstweekday

import calendar

#print(calendar.TextCalendar(firstweekday=6).formatyear(2022))
print(calendar.day_name[0])

indate = "08 05 2015"

date = list(map(int,indate.split()))

print(calendar.day_name[calendar.weekday(date[2], date[0], date[1])].format().upper())