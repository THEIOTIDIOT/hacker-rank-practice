import re

def checkMagazine(magazine, note):
    # Write your code here
    found_word = True
    magazine_dict = {}
    for word in magazine:
        if word not in magazine_dict:
            magazine_dict[word] = 1
        else:
            magazine_dict[word] +=1

    for wrd in note:
        if magazine.get(wrd) >= 0:
            magazine[wrd] -=1
        else:
            found_word = False
            
    if found_word:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    magazine = 'give me one grand today night'
    note = 'give one grand today'

    checkMagazine(magazine, note)