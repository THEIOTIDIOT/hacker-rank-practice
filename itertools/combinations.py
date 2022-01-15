# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations

i = 'HACK 2'.split()

cl = []

sl = list(i[0])
sl.sort()

ss = ''.join(sl)

for index in range(int(i[1])):
    lc =list(combinations(sl,index+1))
    cl.append(lc)

s = ''
cs = []
for l in cl:
    for i in l:
        for j in range(len(i)):
            s += i[j]

        cs.append(s)
        s = ''

print(*cs, sep='\n')