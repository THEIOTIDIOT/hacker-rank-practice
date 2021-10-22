import fileinput
import sys
import re
# Enter your code here. Read input from STDIN. Print output to STDOUT
css = fileinput.input(files='/Users/benjaminzimmer/Documents/GitHub/python_practice/regex1.txt')
contents = ""
hex_values = []
for line in css:
    contents += line

hex_values = re.findall("(:|,| )(#[a-fA-F0-9]{6}|#[a-fA-F0-9]{3})",contents)

for value in hex_values:
    print(value[1])
