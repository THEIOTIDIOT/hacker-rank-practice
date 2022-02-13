# Remarks
# axis = 0 will operate on columns
# axis = 1 will operate on rows
import numpy

r, c = map(int, input().split())

print(numpy.max(numpy.min([list(map(int,input().split())) for _ in range(r)], axis=1)))
