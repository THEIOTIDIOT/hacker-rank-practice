#Difficulty = Medium

def minion_game(string):
    # your code goes here
    # Stuart gets consonants
    # Kevin gets vowels
    # Output is name of winner and score 
    # Draw when there is no winner
    vowels = "AEIOU"
    stuart = 0
    kevin = 0

    for i in range(len(string)):
        if string[i] in vowels:
            kevin += (len(string) - i)
        else:
            stuart += (len(string) - i)


    if stuart == kevin:
        print('Draw')
    elif stuart > kevin:
        print('Stuart {}'.format(str(stuart)))
    elif stuart < kevin:
        print('Kevin {}'.format(str(kevin)))


if __name__ == '__main__':
    s = 'BANANA'#input()
    #with open('hacker-rank-practice/string-manipulation/minion-game-test.txt', 'r') as f:
       # s = f.readline()

    minion_game(s)