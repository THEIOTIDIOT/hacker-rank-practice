import numpy

numpy.set_printoptions(legacy='1.13')
r, c = map(int, input().split())
print(numpy.eye(r, c, k=0))