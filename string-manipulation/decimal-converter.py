def print_formatted(number):
    # your code goes here
    buf = len(bin(number).replace('0b','')) + 1
    line = ''
    string = []
    for i in range(1,number + 1):
        line = (str(i)).rjust(buf-1)+(str(oct(i).replace('0o',''))).rjust(buf)+(str(format(i, 'X'))).rjust(buf)+(str(bin(i).replace('0b',''))).rjust(buf)
        string.append(line)
    print('\n'.join(string))
    

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)