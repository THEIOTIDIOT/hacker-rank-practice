# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
# \1 - negative lookback at the 1st match
# search searches all matches in the string
# match only searches from the beginning of the string
# 
 
m = re.search(r"([a-z0-9])\1+", "12345678910111213141516171820212223")

# m.group(0) returns a list of all matches
# m.groups() returns a list of all matches
print(m.group(1) if m else -1)