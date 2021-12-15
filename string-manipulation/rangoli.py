def print_rangoli(size):
    """ #size 3
        ----c----
        --c-b-c--
        c-b-a-b-c
        --c-b-c--
        ----c----

        #size 8
        --------------h--------------
        ------------h-g-h------------
        ----------h-g-f-g-h----------
        --------h-g-f-e-f-g-h--------
        ------h-g-f-e-d-e-f-g-h------
        ----h-g-f-e-d-c-d-e-f-g-h----
        --h-g-f-e-d-c-b-c-d-e-f-g-h--
        h-g-f-e-d-c-b-a-b-c-d-e-f-g-h
        --h-g-f-e-d-c-b-c-d-e-f-g-h--
        ----h-g-f-e-d-c-d-e-f-g-h----
        ------h-g-f-e-d-e-f-g-h------
        --------h-g-f-e-f-g-h--------
        ----------h-g-f-g-h----------
        ------------h-g-h------------
        --------------h--------------
    """
    # your code goes here
    alphabet = list(map(chr, range(97,123)))
    subset = "".join(alphabet[0:size])

    lines = []
    for i in range(size-1,0,-1):
        lines.append("-".join(subset[::-1][:size-i]+
                                subset[i+1:len(subset)]).center(((size + (size-1))*2)-1,"-"))

    for i in range(0,size):
        lines.append("-".join(subset[::-1][:size-i]+
                                subset[1+i:]).center(((size + (size-1))*2)-1,"-"))
    
    print("\n".join(lines))

    
if __name__ == '__main__':
    #n = int(input())
    print_rangoli(5)
    print_rangoli(3)
    print_rangoli(7)
    print_rangoli(8)