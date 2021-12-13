def print_rangoli(size):
    """ #size 3
        ----c----
        --c-b-c--
        c-b-a-b-c
        --c-b-c--
        ----c----
    """
    # your code goes here
    alphabet = list(map(chr, range(97,123)))
    subset = "".join(alphabet[0:size])

    lines = []
    for i in range(size-1,0,-1):
        lines.append("-".join(subset[::-1][:size-i]+subset[::-1][:size-i-1]).center(size*3,"-"))

    for i in range(0,size):
        lines.append("-".join(subset[::-1][:size-i]+subset[::-1][:size-i-1]).center(size*3,"-"))
    
    print("\n".join(lines))

    
if __name__ == '__main__':
    #n = int(input())
    print_rangoli(3)