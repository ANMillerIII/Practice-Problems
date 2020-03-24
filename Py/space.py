import argparse

class Solution:
    def fib(self, n: int) -> int:
        
        if n < 0:
            
        elif n == 0:
            return 1
        elif n == 1:
            return 1
        else:
            return(Solution.fib(None, n-1) + Solution.fib(None, n-2))
        
print(Solution.fib(None, 0))