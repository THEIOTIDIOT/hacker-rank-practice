import math
import os
import random
import re
import sys

#
# Complete the 'alternatingCharacters' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def alternatingCharacters(s):
    # Write your code here
    counter = 0
    for l in range(len(s)):
        if l + 1 != len(s):
            if s[l] == s[l+1]:
                 counter += 1
           
        
    return counter

if __name__ == "__main__":

    print(alternatingCharacters("ABBABABBB"))
    