import sys
import crypt

# get hash from user
if len(sys.argv) != 2 or not sys.argv[1].isalnum():
    sys.exit("Usage: python crack hash")

# specify salt
hashedPass = sys.argv[1]
salt = sys.argv[1][0:2]

# generate asc
asc = list(range(0, 1)) + list(range(65, 91)) + list(range(97, 123))

# initialize password guess
guess = ''

# loop over all possible strings to length 4


def main():
    for a in asc:
        for b in asc:
            for c in asc:
                for d in asc:
                    guess = guess if a == 0 else guess + chr(a)
                    guess = guess if b == 0 else guess + chr(b)
                    guess = guess if c == 0 else guess + chr(c)
                    guess = guess if d == 0 else guess + chr(d)
                    if compare:
                        print(guess)
                        break
                    guess = ''
                    if compare:
                        break
                if compare:
                    break
            if compare:
                break
        if compare:
            break


def compare():
    return crypt.crypt(guess, salt) == hashedPass


if __name__ == "__main__":
    main()