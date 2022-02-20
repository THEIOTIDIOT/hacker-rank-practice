import math
import os
import random
import re
import sys

def timeConversion(s):
    # Write your code here
    if re.search("(PM$)", s) != None:
        if s[0:2] == '12':
            return s[:-2]
        return str(int(s[0:2])+12) + s[2:-2]
    else:
        if s[0:2] == '12':
            s = '00' + s[2:-2]
            return s 
    return s[:-2]


if __name__ == '__main__':
    print(timeConversion("12:45:54PM"))
    