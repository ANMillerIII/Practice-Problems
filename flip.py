# doesn't find fastest x flips to solve xxxyyyy
def flip(s):
    sList = list(s)
    count = 0
    while True:
        for index, char in enumerate(sList):
            if char == 'y' and 'x' in sList[index:]:
                sList[index] = 'x'
                count += 1
            elif char == 'y' and not 'x' in sList[index:]:
                return count
            elif char == 'x' and 'y' in sList:
                pass
            elif 'y' not in sList or 'x' not in sList:
                return count
            else:
                pass

print(flip('xxyyxxxy'))
print(flip('xxyyyyy'))
print(flip('yxyyyyy'))
print(flip('xxyxyy'))
print(flip('xxxx'))
print(flip('yyyyy'))
print(flip('xxyyxyxyxyyyyy'))
print(flip('xxyyyyxxxyy'))
print(flip('xxyyxyyy'))
