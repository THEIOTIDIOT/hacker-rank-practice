from collections import Counter
"""This program will take a string input 
of at least 3 distinct letters or more and 
list the top three occuring letters in the string. 
When there are two of the top three letters that
are equal - ensure these letters are listed alphabetically"""

if __name__ == '__main__':
    string = input()
    counted = Counter(sorted(string))
    mc = counted.most_common(3)
    for i in range(3):
        print(mc[i][0] + ' ' + str(mc[i][1]))