import sys
from cs50 import get_string


def main():
    # Check if input is good
    if len(sys.argv) != 2:
        sys.exit("Usage: python bleep words.txt")
    banned = sys.argv[1]
    # Call get message, load and censor functions
    text = getCensor()
    words = load(banned)
    censor(text, words)
    return True

# Get message to censor


def getCensor():
    censor = get_string("What message would you like to censor?\n")
    return censor.split(' ')

# Load bad words


def load(banned):
    words = []
    file = open(banned, "r")
    for line in file:
        words.append(line.rstrip("\n"))
    file.close()
    return words

# Censor bad words


def censor(text, words):
    word = []
    count = 0
    for word in text:
        if word.lower() in words:
            text[count] = ""
            for letters in word:
                text[count] += "*"
        count += 1      # How to get rid of count/index?
    # Stringify
    print(f"{' '.join(text)}")


if __name__ == "__main__":
    main()