# Strobogrammatic 

import time

class Solution:
    def strobo(self, num):
        start = time.time()
        sNum = str(num)
        for index, digit in enumerate(sNum):
            if digit == "1" or digit == "8":
                if digit != sNum[len(sNum)-1-index]:
                    return False
            elif digit == "6":
                if sNum[len(sNum)-1-index] != "9":
                    return False
            elif digit == "9":
                if sNum[len(sNum)-1-index] != "6":
                    return False
            else:
                return False
        time.sleep(.1)
        end = time.time()
        return True
        

assert(Solution.strobo(None, 123)) == False
assert(Solution.strobo(None, 111)) == True
assert(Solution.strobo(None, 181)) == True
assert(Solution.strobo(None, 916)) == True
assert(Solution.strobo(None, 123)) == False
assert(Solution.strobo(None, 111)) == True
assert(Solution.strobo(None, 181)) == True
assert(Solution.strobo(None, 916)) == True