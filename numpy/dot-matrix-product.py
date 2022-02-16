import numpy

# WTH is a dot product?!?! 
# https://en.wikipedia.org/wiki/Dot_product
# Algebraically it is defined as such :
#   1-D arrays
#   a = [1, 2]
#   b = [3, 4]
#   dot product = a1*b1 + a2*b2 = 11
#   
#   2-D arrays
#   If both a and b are 2-D arrays, it is matrix multiplication

n = int(input())
a = list()
b = list()
for _ in range(n):
    a.append(list(map(int, input().split())))

for _ in range(n):
    b.append(list(map(int, input().split())))
    
print(numpy.dot(a,b))