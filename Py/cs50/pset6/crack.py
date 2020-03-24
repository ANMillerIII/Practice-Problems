import sys
import crypt

# get hash from user
if len(sys.argv) != 2 or not sys.argv[1].isalnum():
    sys.exit("Usage: python crack hash")

# loop over all possible strings to length 4


def main():
    # generate asc
    asc = list(range(0, 1)) + list(range(65, 91)) + list(range(97, 123))

    # initialize password guess
    guess = ''
    for a in asc:
        for b in asc:
            for c in asc:
                for d in asc:
                    guess = guess if a == 0 else guess + chr(a)
                    guess = guess if b == 0 else guess + chr(b)
                    guess = guess if c == 0 else guess + chr(c)
                    guess = guess if d == 0 else guess + chr(d)
                    if compare(guess):
                        print(guess)
                        break
                    guess = ''
                    if compare(guess):
                        break
                if compare(guess):
                    break
            if compare(guess):
                break
        if compare(guess):
            break

# compare guess to hashedPass


def compare(guess):
    # specify salt
    hashedPass = sys.argv[1]
    salt = sys.argv[1][0:2]
    return crypt.crypt(guess, salt) == hashedPass


if __name__ == "__main__":
    main()