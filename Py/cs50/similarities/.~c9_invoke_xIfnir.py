import io
from nltk.tokenize import sent_tokenize

# Return lines in both a and b
def lines(a, b):
    aLines = []
    bLines = []
    with open(a, "r") as file:
        for line in file.readlines():
            aLines.append(line.rstrip())
    with open(b, "r") as file:
        for line in file.readlines():
            bLines.append(line.rstrip())
    similarities = []
    repeats = []
    for element in aLines:
        if element in bLines and (element not in repeats):
            similarities.append(element)
            repeats.append(element)
    return similarities

# Return sentences in both a and b
def sentences(a, b):
    aFile = open("a.txt").read()
    aSents = sent_tokenize(aFile)
    bFile = open("b.txt").read()
    bSents = sent_tokenize(bFile)
    repeats = []
    similarities = []
    for element in aSents:
        if element in bSents and (element not in repeats):
            similarities.append(element)
            repeats.append(element)
    return similarities

# sentences("a.txt", "b.txt")

# Return substrings of length n in both a and b
def substrings(a, b, n):
    string = "hello"
    aString = 
    n = 2
    length = len(string)
    # subs = [string[ i : j + 1] for i in range(length) for j in range(i,length)]
    # for sub in subs:
    #     print(f"{sub,len(sub)}")
    #     if len(sub) != n:
    #         subs.remove(sub)
    #         print(f"{subs}")
    # print(f"{subs}")

substrings(1,2,3)