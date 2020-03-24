import io
from nltk.tokenize import sent_tokenize

# Return lines in both a and b


def lines(a, b):
    aLines = a.splitlines(0)
    bLines = b.splitlines(0)
    similarities = []
    repeats = []
    for element in aLines:
        if element in bLines and (element not in repeats):
            similarities.append(element)
            repeats.append(element)
    return similarities

# Return sentences in both a and b


def sentences(a, b):
    aSents = sent_tokenize(a)
    bSents = sent_tokenize(b)
    repeats = []
    similarities = []
    for element in aSents:
        if element in bSents and (element not in repeats):
            similarities.append(element)
            repeats.append(element)
    return similarities


# Return substrings of length n in both a and b


def substrings(a, b, n):
    aSubs = []
    bSubs = []
    for i, x in enumerate(a):
        for j, z in enumerate(a):
            if len(a[i:j+1]) == n:
                aSubs.append(a[i:j+1])
    for i, x in enumerate(b):
        for j, z in enumerate(b):
            if len(b[i:j+1]) == n:
                bSubs.append(b[i:j+1])
    repeats = []
    similarities = []
    for element in aSubs:
        if element in bSubs and (element not in repeats):
            similarities.append(element)
            repeats.append(element)
    return similarities