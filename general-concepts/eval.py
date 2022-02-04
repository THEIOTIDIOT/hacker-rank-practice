inp = """1 4
x**3 + x**2 + x + 1
"""

i = list(map(int,input().split()))
x = i[0]
y = i[1]

print("True" if eval(input()) == y else "False")
