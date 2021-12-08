if __name__ == '__main__':
    # Enter your code here. Read input from STDIN. Print output to STDOUT
    inp = input().split()
    n = int(inp[0])
    m = int(inp[1])

    def printmat(n,m):
    
        welcs = 'WELCOME'.center(m,'-')
        sym = '.|.'
        for i in range(1,(n//2)*2,2):
            print((sym*i).center(m,'-'))
        
        print(welcs)
    
        for i in range((n//2)*2, 1, -2):
            print((sym*(i-1)).center(m, '-'))

    printmat(n,m)