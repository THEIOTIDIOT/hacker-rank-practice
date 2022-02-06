
# Positive Lookahead
# (?=...)
# Asserts that the given subpattern can be matched here, 
# without consuming characters
# r'foo(?=bar)'
# (foo)bar foobaz

import re

s = 'aaadaa'
k = 'aa'
if k in s:
    print(*[(i.start(), (i.start()+len(k)-1)) for i in re.finditer(r'(?={})'.format(k), s)], sep='\n')
else:
    print('(-1, -1)')