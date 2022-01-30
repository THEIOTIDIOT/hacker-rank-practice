# issuperset(other) or
# set >= other
# Test whether every element in other is in the set.

# Strict Superset
# set > other
# Test whether the set is a proper superset of other, 
# that is, set >= other and set != other.

# Enter your code here. Read input from STDIN. Print output to STDOUT
setA = set(input().split())
ans = []
for _ in range(int(input())):
    setB = set(input().split())
    ans.append(True if setA > setB else False)
    
print(all(ans))
