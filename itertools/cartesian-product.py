#You are given a two lists  and . Your task is to compute their cartesian product X.
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

A = list(map(int, input().split()))
B = list(map(int, input().split()))

print(*list(product(A,B)), sep=' ')