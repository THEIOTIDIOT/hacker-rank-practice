if __name__ == '__main__':
    # Enter your code here. Read input from STDIN. Print output to STDOUT
    input()
    ints = list(map(int,input().split()))
    a = set(map(int, input().split()))
    b = set(map(int, input().split()))
    happiness = 0
    for s in ints:
        if s in a:
            happiness += 1
        elif s in b:
            happiness -= 1
    
    print(happiness)