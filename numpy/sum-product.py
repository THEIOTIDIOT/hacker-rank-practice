import numpy

test='''2 2
1 2
3 4'''

r, c = map(int, input().split())

a = numpy.array([list(map(int, input().split())) for _ in range(r)])

print(numpy.product(numpy.sum(a, axis=0), axis=0))