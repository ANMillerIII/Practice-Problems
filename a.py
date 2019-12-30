#find all substrings in string

def main(s):
    return [s[i:k] for i in range(len(s)) for k in range(i+1, len(s)+1)]

if __name__=="__main__":
    # print(main('apples are coolio'))
    print(main('hey'))
    print(main('yo'))
    print(main('what'))























# for every possible combination (in existing order) of letters in string
    # if combination is not in list of subs, and length is less than string length
        # add to list of substrings

# traverse entire string every time (brute force)