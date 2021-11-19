import math

def makeAnagram(a, b):
    # Write your code here
    deleted = len(a) + len(b)

    la = [l for l in a if l in b]
    lb = [l for l in b if l in a]

    deleted -= len(la) + len(lb)
    la.sort()
    last_ltr = ""
    for l in la:
        if last_ltr != l:
            ac = la.count(l)
            bc = lb.count(l)
            deleted += abs(ac-bc)
        last_ltr = l
        
    return deleted

def tests():
    a = ["showman", "cde", "fcrxzwscanmligyxyvym", ]
    b = ["woman", "abc", "jxwtrhvujlmrpdoqbisbwhmgpmeoke"]
    answer = [2,4,30]
    
    for i in range(len(a)):
        assert makeAnagram(a[i],b[i]) == answer[i], "Failed"
if __name__ == "__main__":
    tests()
    print("Passed")