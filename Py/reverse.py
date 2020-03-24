import sys

class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            reversed = int(str(x)[::-1].replace('-',''))*-1
        else:
            reversed = int(str(x)[::-1])
        if abs(reversed) > 2**31-1:
            return 0
        else:
            return reversed
        

Solution.reverse(None,154354523525)