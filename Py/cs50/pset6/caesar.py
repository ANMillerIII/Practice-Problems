import sys
from cs50 import get_string

# get key as commandline argument
if len(sys.argv) != 2:
    sys.exit("Usage: python caesar.py key")
k = int(sys.argv[1])

# get plaintext
p = get_string("plaintext: ")


# for character in plaintext, get the # associated
listP = []
for c in p:
    listP.append((ord(c)))

# shift each # by key, wrapping if necessary
# count = 0
for n,i in enumerate(listP):
    if i >= 65 and i <= 90:
        listP[n] = (i + k - 65) % 26 + 65
    elif i >= 97 and i <= 122:
        listP[n] = (i + k - 97) % 26 + 97
    # count += 1

# make into list of chars, stringify, print
listC = []
for i in listP:
    listC.append(chr(i))
print(f"ciphertext: {''.join(listC)}")
