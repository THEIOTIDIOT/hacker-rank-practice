# Enter your code here. Read input from STDIN. Print output to STDOUT

# returns numbers only in both sets - len is useful
s = set([1,2,3,4,5,6,7,8,9])
print(len(s.union(set([10,1,2,3,11,21,55,6,8]))))