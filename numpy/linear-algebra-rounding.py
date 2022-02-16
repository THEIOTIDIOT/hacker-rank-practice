import numpy

n = int(input())
a = list()
for _ in range(n):
    a.append(list(map(float, input().split())))

print('{}'.format(numpy.linalg.det(a).round(2)))