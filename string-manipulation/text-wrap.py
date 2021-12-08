

if __name__ == '__main__':

    def wrap(string, max_width):
    
        strarr = [string[i:i+max_width] for i in range(0,len(string),max_width)]
        return "\n".join(strarr)

    print(wrap('123412341234', 4))