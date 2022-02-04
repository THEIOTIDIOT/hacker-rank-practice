inp="""5
12 9 61 5 14"""
# Checks if the integers are all positive and any of the integers are palindromic
# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
l = list(map(int, input().split()))
pos = list()
palindromic = list()
for i in l:
    pos.append(True if i >= 0 else False)
    palindromic.append(True if str(i) == ''.join(reversed(str(i))) else False)
    
print("True" if all(pos) and any(palindromic) else "False")