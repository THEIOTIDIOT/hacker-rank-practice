def merge_the_tools(string, k):
    # your code goes here
    i = 0
    letters = ''
    for s in string:

        i += 1

        if s not in letters:
            letters += s

        if i == k:
            print(letters)
            letters = ''
            i = 0
        
if __name__ == '__main__':
    #string, k = input(), int(input())
    merge_the_tools('AABCAAADA', 3)