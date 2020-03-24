from cs50 import get_string

# get # from user, check if valid input


def getNum():
    while True:
        ccNum = get_string("CC Number: ")
        if ccNum.isdigit():
            return ccNum

# once valid, check if LUHNS is good


def luhn(ccNum):
    ccLuhn = ccNum[len(ccNum)-2::-2]
    ccLuhn2 = ccNum[len(ccNum)-1::-2]
    a = 0
    b = 0
    for c in ccLuhn:
        a += 2*int(c) // 10 + 2*int(c) % 10
    for c in ccLuhn2:
        b += int(c)
    luhns = (a + b) % 10
    if (luhns == 0):
        return True
    return False

# once luhns is good, check other things


def cardType(ccNum):
    ccLen = len(ccNum)
    first = int(ccNum[0])
    second = int(ccNum[1])
    print(f"{ccNum[0]}{ccLen}")
    if ccLen == 15 and first == 3 and (second == 4 or second and 7):
        print("AMEX")
    elif ccLen == 16 and first == 5 and (second >= 1 and second <= 5):
        print("MASTERCARD")
    elif (ccLen >= 13 and ccLen <= 16) and first == 4:
        print("VISA")
    else:
        print("INVALID")
    return True


# driver
ccNum = getNum();
if luhn(ccNum):
    cardType(ccNum)
else:
    print("INVALID")
