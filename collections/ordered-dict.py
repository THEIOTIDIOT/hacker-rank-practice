testcase1 = '''
9
BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
items = int(input())
od = OrderedDict()

for _ in range(items):
    line = input().split()
    num = int(line[-1])
    del line[-1]
    item = ' '.join(line)
    if item not in od:
        od[item] = num
    else:
        od[item] += num

for key, value in od.items():
    print(key, str(value), sep=' ')