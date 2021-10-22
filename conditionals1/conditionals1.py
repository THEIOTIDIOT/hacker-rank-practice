import math

if __name__ == '__main__':
    n = int(input().strip())
    weird = "Weird"
    not_weird = "Not Weird"
    if n % 2 > 0:
        print(weird)
    elif n in range(1,6):
        print(not_weird)
    elif n in range(5,21):
        print(weird)
    elif n > 20:
        print(not_weird)