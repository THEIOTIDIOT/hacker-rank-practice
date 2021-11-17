def makeAnagram(a, b):
    # Write your code here
    deleted = len(a) + len(b)

    len(a.strip(b))
    b = b.strip(a)
            
    return deleted - len(a) - len(b)

if __name__ == "__main__":

    a = "fcrxzwscanmligyxyvym"
    b = "jxwtrhvujlmrpdoqbisbwhmgpmeoke"

    print(makeAnagram(a,b))