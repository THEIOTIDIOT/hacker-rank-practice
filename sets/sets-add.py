# loops through input and prints a count of the unique elements
"""
7
UK
China
USA
France
New Zealand
UK
France 
"""
cs = set()
for _ in range(int(input())):
    cs.add(input())
    
print(len(cs))