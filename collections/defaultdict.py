# Enter your code here. Read input from STDIN. Print output to STDOUT
# input 
# line1 - group a size - group b size
# line2 - line x - word group A
# linex - line x - word group B

from collections import defaultdict
ll = input().split()
asize = int(ll[0])
bsize = int(ll[1])
add = defaultdict(list)
for i in range(1,asize + 1):
    add[input()].append(i)
    
for i in range(bsize):
    letter = input()
    if len(add[letter]) == 0:
        print('-1')
    else:
        print(*add[letter], sep=' ')
    