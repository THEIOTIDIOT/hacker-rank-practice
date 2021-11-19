#
# Complete the 'twoStrings' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def twoStrings(s1, s2):
    # Write your code here
    s1_perms = {}
    for i in range(len(s1)):
        for j in range(len(s1) - i):
            if j == 0:
                perm = s1[i:]
            else:
                perm = s1[i:j*-1]
            
            if perm not in s1_perms:
                s1_perms[perm] = 1
            else:
                s1_perms[perm] += 1
    print(s1_perms)
    for k in range(len(s2)):
        for l in range(len(s2)-k):
            if l == 0:
                perm = s2[k:]
            else:
                perm = s2[k:l*-1]
                
            if perm in s1_perms:
                return "YES"
            
    return "NO"

if __name__ == '__main__':
        
    print(twoStrings('hello','world'))