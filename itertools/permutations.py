
#Task

#You are given a string .
#Your task is to print all possible permutations of size of the string in lexicographic sorted order.

#Input Format

#A single line containing the space separated string  and the integer value .

# Test Case = HACK 2
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations


#i = input().split()
i = "HACK 2".split()
l = list(permutations(i[0], int(i[1])))
ls = []
for item in l:
    s =''
    for letter in item:
        s += letter
    if s not in ls:
        ls.append(s)

ls.sort()
print(*ls, sep='\n')

