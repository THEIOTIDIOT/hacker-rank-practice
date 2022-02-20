'''
2
Sun 10 May 2015 13:54:36 -0700
Sun 10 May 2015 13:54:36 -0000
Sat 02 May 2015 19:54:36 +0530
Fri 01 May 2015 13:54:36 -0000

STRPTIME
classmethod datetime.strptime(date_string, format)
Return a datetime corresponding to date_string, parsed according to format.

This is equivalent to:

datetime(*(time.strptime(date_string, format)[0:6]))
ValueError is raised if the date_string and format can't be parsed by time.strptime() 
or if it returns a value which isn’t a time tuple. For a complete list of formatting 
directives, see strftime() and strptime() Behavior.
'''

#!/bin/python3

import math
import os
import random
import re
import sys

from datetime import timedelta, timezone, date, datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    #https://docs.python.org/3.9/library/datetime.html#strftime-strptime-behavior
    
    #print(' '.join(t1.split()[1:]))
    #ts1 = datetime.strptime(' '.join(t1.split()[1:]), '%d %b %Y %X %z')
    #ts2 = datetime.strptime(' '.join(t1.split()[1:]), '%d %b %Y %X %z')

    ts1 = datetime.strptime(t1, '%a %d %b %Y %X %z')
    ts2 = datetime.strptime(t2, '%a %d %b %Y %X %z')
    nt1 = ts1.astimezone(timezone.utc)
    nt2 = ts2.astimezone(timezone.utc)

    s1 = (nt1 - datetime(1970, 1, 1, tzinfo=timezone.utc)).total_seconds()
    s2 = (nt2 - datetime(1970, 1, 1, tzinfo=timezone.utc)).total_seconds()
    return str(abs(int(s1-s2)))

if __name__ == '__main__':
    with open('hacker-rank-practice/datetime/time-delta.txt','r') as f:

        for i in range(int(f.readline().replace('\n', ''))):
            t1 = f.readline().replace('\n', '')
            t2 = f.readline().replace('\n', '')

            print(time_delta(t1, t2))
            #time_delta(t1, t2)


    #time_delta('Sun 10 May 2015 13:54:36 -0700','Sun 10 May 2015 13:54:36 -0000')
