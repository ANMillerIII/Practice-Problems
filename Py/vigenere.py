import sys


# get key as commandline argument
if len(sys.argv) != 2 or not sys.argv[1].isalpha():
    sys.exit("Usage: python vigenere.py key")
listK = list(sys.argv[1])

# fix key
for n, i in enumerate(listK):
    listK[n] = ord(i)
    if listK[n] >= 65 and listK[n] <= 90:
        listK[n] -= 65
    elif listK[n] >= 97 and listK[n] <= 122:
        listK[n] -= 97


# get plaintext
p = input("plaintext: ")

# for character in plaintext, get the # associated
listP = []
for c in p:
    listP.append((ord(c)))

# shift each # by key, wrapping if necessary
count = 0
for n, i in enumerate(listP):
    if i >= 65 and i <= 90:
        listP[n] = (i + listK[n % len(listK)] - 65) % 26 + 65
    elif i >= 97 and i <= 122:
        listP[n] = (i + listK[n % len(listK)] - 97) % 26 + 97
    else:
        n = n-1
# make into list of chars, stringify, print
listC = []
for i in listP:
    listC.append(chr(i))
print(f"ciphertext: {''.join(listC)}")
