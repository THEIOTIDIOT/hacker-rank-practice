# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

now = int(input())
od = OrderedDict()
for _ in range(now):
    word = input()
    if word not in od:
        od[word] = 1
    else:
        od[word] += 1
        
print(len(od))
print(' '.join(list(map(str, od.values()))))