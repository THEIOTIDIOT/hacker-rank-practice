import numpy

numpy.set_printoptions(legacy='1.13')

a = numpy.array(list(map(float, '1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9'.split())))

print(numpy.floor(a))
print(numpy.ceil(a))
print(numpy.rint(a))