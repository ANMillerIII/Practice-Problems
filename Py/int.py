# Write an algorithm that finds the total number of set bits in all integers between 1 and N.
import sys

class Solution:
    def num(self, n: int) -> int:
        setBits = 0
        for num in range(1,n+1):
            biNum = bin(num)[2:]
            for bit in biNum:
                if bit is not '0':
                    setBits += 1
        return setBits

print(Solution.num(None, 5))
















# eg. n =2 should return (1, 10) --> 1+1 = 2, 3 would be (1, 10, 11) 1+1+2 = 4
# int has 4 bytes, or 16 or 32 bit
# set bit is a 1
# how convert int to binary?
# bin()


