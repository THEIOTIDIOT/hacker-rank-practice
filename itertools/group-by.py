#https://docs.python.org/2/library/itertools.html#itertools.groupby
    # [k for k, g in groupby('AAAABBBCCDAABBB')] --> A B C D A B
    # [list(g) for k, g in groupby('AAAABBBCCD')] --> AAAA BBB CC D
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby

s = '11111222229999900008888'
print(*[(len(list(g)),int(k)) for k, g in groupby(s)], sep=' ')