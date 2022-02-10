# A valid UID must follow the rules below:

# It must contain at least 2 uppercase English alphabet characters.
# It must contain at least 3 digits (0 - 9).
# It should only contain alphanumeric characters (a - z, A - Z & 0 - 9).
# No character should repeat.
# There must be exactly 10 characters in a valid UID.

# Notes 
# [A-Za-z0-9]{10} - ensures there are 10 characters
# ([A-Z].*){2} - has 2 or more A-Z chars

import re

with open('/Users/benjaminzimmer/Documents/GitHub/hacker-rank-practice/regex-parsers/uid-validation-tests.txt', 'r') as f:

    for _ in range(int(f.readline())):
        s = f.readline()
    
        print('Valid' if all(\
            [re.search(r, s) for r in \
                [r'[A-Za-z0-9]{10}', r'([A-Z].*){2}', r'([0-9].*){3}']])\
                     and not re.search(r'.*(.).*\1', s) else 'Invalid')

