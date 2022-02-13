# Remarks
# axis = 0 will operate on columns
# axis = 1 will operate on rows
import numpy
r, c = map(int, input().split())
a = numpy.array([list(map(int,input().split())) for _ in range(r)], dtype=numpy.int32)
print(numpy.mean(a, axis=1))
print(numpy.var(a, axis=0))

# formats the float to have 11 decimal places if the mantissa/significant digits are that precise
print(float('{:.11f}'.format(numpy.std(a))))
