import sys
from cs50 import get_string

# get key as commandline argument
k = sys.argv[1]
if len(sys.argv) != 2 or not k.isalpha():
    sys.exit("Usage: python vigenere.py key")

# Make key into adjusted list
listK = list(k)
for n, i in enumerate(listK):
    listK[n] = ord(i)
    if listK[n] >= 65 and listK[n] <= 90:
        listK[n] -= 65
    elif listK[n] >= 97 and listK[n] <= 122:
        listK[n] -= 97

# get plaintext
p = get_string("plaintext: ")

# for character in plaintext, get the # associated
listP = []
for c in p:
    listP.append((ord(c)))

# shift each # by key, wrapping if necessary
for n, i in enumerate(listP):
    if i >= 65 and i <= 90:
        listP[n] = (i + listK[n % len(listK)] - 65) % 26 + 65
    elif i >= 97 and i <= 122:
        listP[n] = (i + listK[n % len(listK)] - 97) % 26 + 97
    else:
        listP[n] = listP[n]

# make into list of chars, stringify, print
listC = []
for i in listP:
    listC.append(chr(i))
print(f"ciphertext: {''.join(listC)}")
