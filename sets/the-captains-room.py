# Enter your code here. Read input from STDIN. Print output to STDOUT
test="""
5
1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2 
"""

# finds the number that is not duplicated - the captains room

input()
a = input().split()
s1 = set()
s2 = set()

for e in a:
    if e in s1:
        s2.add(e) # this one gets duplicates
    else:
        s1.add(e) # this one gets everything
s1.difference_update(s2)
print(list(s1)[0])