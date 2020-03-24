def subString(Str,n):
    for Len in range(1,n + 1):
        for i in range(n + 1):
            j = i + Len - 1
            for k in range(i,j + 1):
                print(Str[k],end="")
            print()

Str = "abc"
subString(Str,2)