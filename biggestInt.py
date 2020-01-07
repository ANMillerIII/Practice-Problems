# 1/7/20

# Given an integer n, # find the next biggest integer with the same number 
# of 1-bits on. For example, given the number 6 (0110 in binary),
#  return 9 (1001).

class Solution:
    def main(self, n):
        ones = str(bin(n)[2:]).count('1')
        nextInt = n + 1
        while True:
            nextOnes = str(bin(nextInt)[2:]).count('1')
            if nextOnes == ones:
                return nextInt
            nextInt += 1

if __name__=="__main__":
    assert(Solution.main(None, 6)) == 9
    assert(Solution.main(None, 9)) == 10
    assert(Solution.main(None, 23)) == 27
    
