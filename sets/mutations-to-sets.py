# .update() or |= 
# both operators to make mutations to a set
# set.update(another_set) - mutates the first set

# .intersection_update() or &=
# Update the set by keeping only the elements found in it and an iterable/another set.

# .difference_update() or -=
# Update the set by removing elements found in an iterable/another set.

# .symmetric_difference_update() or ^=
# Update the set by only keeping the elements found in either set, but not in both

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
s = set(map(int, input().split()))

nops = int(input())

for _ in range(nops):
    cmds = input().split()
    cmd = cmds[0]
    args = set(map(int, input().split()))
    
    if cmd == "intersection_update":
        s.intersection_update(args)
    elif cmd == "difference_update":
        s.difference_update(args)
    elif cmd == "symmetric_difference_update":
        s.symmetric_difference_update(args)
    elif cmd == "update":
        s.update(args)
    
print(sum(s))