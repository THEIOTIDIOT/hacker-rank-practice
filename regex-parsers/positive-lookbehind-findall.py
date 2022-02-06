# (?<=...)
# Ensures that the given pattern will match, 
# ending at the current position in the expression. 
# The pattern must have a fixed width. Does not consume any characters.
# /(?<=foo)bar/
# foo(bar) fuubar "() == match"

# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

matches = re.findall(r'(?<=[bcdfghjklmnpqrstvxyz])([aeiou]{2,})[bcdfghjklmnpqrstvxyz]',
input(),flags = re.I)

print('\n'.join(matches) if len(matches) > 0 else -1)