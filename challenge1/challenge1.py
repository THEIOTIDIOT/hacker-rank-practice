#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here 
    count = len(arr)
    neg = float(0)
    zero = float(0)
    pos = float(0)
    
    for num in arr:
        if num == 0:
            zero += 1
        elif num < 0:
            neg += 1
        elif num > 0:
            pos += 1
    if count == 0:
        print("{:.6f}".format(float(0)))
        print("{:.6f}".format(float(0)))
        print("{:.6f}".format(float(0)))
    else:
        print("{:.6f}".format(pos/count))
        print("{:.6f}".format(neg/count))
        print("{:.6f}".format(zero/count)) 

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)