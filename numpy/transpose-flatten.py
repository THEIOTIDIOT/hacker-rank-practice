import numpy

nm = list(map(int, input().split()))
n = nm[0]
m = nm[1]

a = numpy.array([list(map(int, input().split())) for _ in range(n)])
print(numpy.transpose(a))
print(a.flatten())