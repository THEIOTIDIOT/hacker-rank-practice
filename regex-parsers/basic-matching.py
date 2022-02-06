# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = int(1)

# number is 10 digits long and starts with 7 8 or 9
for _ in range(n):
    print('YES' if re.match(r'^[789][0123456789]{9}$', '9587456281') else 'NO')