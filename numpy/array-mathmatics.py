import numpy

r, c = map(int, input().split())

a = numpy.array([list(map(int, input().split())) for _ in range(r)])

b = numpy.array([list(map(int, input().split())) for _ in range(r)])

print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print(a**b)