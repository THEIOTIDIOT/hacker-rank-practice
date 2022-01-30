# Enter your code here. Read input from STDIN. Print output to STDOUT

# is set A a subset of set B??
# issubset() is used to check if all elements in A are in B
cases = int(input())

for _ in range(cases):
    input()
    setA = set(map(int,input().split()))
    input()
    setB = set(map(int,input().split()))
    print("True" if setA.issubset(setB) else "False")