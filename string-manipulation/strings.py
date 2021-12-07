if __name__ == '__main__':
    s = input()
    st = [s for s in range(5)]
    res = [False for j in range(5)]
    for i in range(len(st)):
        flag = False
        for j in range(len(s)):
            if i == 0:
                flag = True if s[j].isalnum() else False
            elif i == 1:
                flag = True if s[j].isalpha() else False
            elif i == 2:
                flag =True if s[j].isdigit() else False
            elif i == 3:
                flag = True if s[j].islower() else False
            elif i == 4:
                flag = True if s[j].isupper() else False
        res[i] = flag
    
    print("\n".join(str(e) for e in res))