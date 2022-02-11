def wrapper(f):
    
    def fun(l):
        # complete the function
        nums = list()
        for num in l:
            if len(num) == 10:
                nums.append('{} {} {}'.format('+91', num[:5], num[5:]))
            elif len(num) == 11:
                nums.append('{} {} {}'.format('+91', num[1:6], num[6:]))
            elif len(num) == 12:
                nums.append('{} {} {}'.format('+91', num[2:7], num[7:]))
            else:
                nums.append('{} {} {}'.format('+91', num[3:8], num[8:]))

        return f(nums)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    with open('/Users/benjaminzimmer/Documents/GitHub/hacker-rank-practice/decorators/test-input.txt', 'r', newline=None) as f:
        n = f.readline()
        l = [f.readline().replace('\n', '') for _ in range(int(n))]
        sort_phone(l) 