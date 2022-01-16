# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement
s = 'HACK 2'.split()
it = list(s[0])
it.sort()

cwr = list(combinations_with_replacement(''.join(it), int((s[1]))))

for row in cwr:
    s = ''
    for col in row:
        s += col
    print(s)
