import math

def repeatedString(s, n):
    # Write your code here
    if n % len(s) == 0:
        return s.count('a') * int(n/len(s))
    else:
        rem = n % len(s)
        ayes = math.floor(n / len(s)) * s.count('a')
        ayes += s[0:rem].count('a')
        return ayes

if __name__ == '__main__':
    s = 'kmretasscityylpdhuwjirnqimlkcgxubxmsxpypgzxtenweirknjtasxtvxemtwxuarabssvqdnktqadhyktagjxoanknhgilnm'
    n = 736778906400

    print(repeatedString(s,n))