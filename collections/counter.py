# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
# line1 - number of shoes
# line2 - line containing each shoe id'd by size
# line3 - number of custs
# line4-linex - potential sales (size, price)

nos = int(input())
los = list(input().split())
noc = int(input())
shoecounts = Counter(los)
sck = list(map(int,shoecounts.keys()))
scv = list(map(int,shoecounts.values()))
totalprice = 0
for item in range(noc):
    line = input().split()
    linel = list(map(int,line))
    sizeneeded = linel[0]
    price = linel[1]
    for sizeindex in range(len(sck)):
        if sck[sizeindex] == sizeneeded:
            if scv[sizeindex] > 0:
                totalprice += price
                scv[sizeindex] -= 1
            
print(totalprice)