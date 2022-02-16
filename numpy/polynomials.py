import numpy
test='''
1.1 2 3
0
'''
ans=3
print(numpy.polyval(list(map(float, input().split())), int(input())))