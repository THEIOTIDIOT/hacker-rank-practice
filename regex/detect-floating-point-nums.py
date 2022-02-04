
inp="""
✔ +4.50
✔ -1.0
✔ .5
✔ -.7
✔ +.4
✖ -+4.5
"""

"""
^[-+]?[0-9]*\.[0-9]+$
^ asserts position at start of the string
Match a single character present in the list below [-+]
? matches the previous token between zero and one times, as many times as possible, giving back as needed (greedy)
-+ matches a single character in the list -+ (case sensitive)
Match a single character present in the list below [0-9]
* matches the previous token between zero and unlimited times, as many times as possible, giving back as needed (greedy)
0-9 matches a single character in the range between 0 (index 48) and 9 (index 57) (case sensitive)
\. matches the character . with index 4610 (2E16 or 568) literally (case sensitive)
Match a single character present in the list below [0-9]
+ matches the previous token between one and unlimited times, as many times as possible, giving back as needed (greedy)
0-9 matches a single character in the range between 0 (index 48) and 9 (index 57) (case sensitive)
$ asserts position at the end of the string, or before the line terminator right at the end of the string (if any)
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

for _ in range(int(input())):
    print(bool(re.match("^[-+]?[0-9]*\.[0-9]+$", input())))