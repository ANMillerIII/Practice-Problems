def repeatedChar(string):
    repeats = []
    for char in string:
        if char in repeats:
            return char
        repeats.append(char)

print(repeatedChar("ABCDEFGB"))