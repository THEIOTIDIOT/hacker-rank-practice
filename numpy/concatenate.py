import numpy

with open('/Users/benjaminzimmer/Documents/GitHub/hacker-rank-practice/numpy/concatenate-test.txt', 'r') as f:
    n, m, p = map(int, f.readline().replace('\n', '').split())

    a = [numpy.array(f.readline().replace('\n', '').split(), int) for _ in range(n)]
    b = [numpy.array(f.readline().replace('\n', '').split(), int) for _ in range(m)]

    print(numpy.concatenate((a, b), axis=0))