# 1/8/20

# Given an array of numbers and a number k, determine 
# if there are three entries in the array which add up 
# to the specified number k. For example, given [20, 303, 3, 4, 25] 
# and k = 49, return true as 20 + 4 + 25 = 49.

# O(n) solution, n is length of the array. Traverses array in linear time.

class Solution:
    def __init__(self, array, k):
        self.array = array
        self.k = k
        
    def main(self, array, k):
        for p1, i in enumerate(array):
            for p2, j in enumerate(array):
                for p3, x in enumerate(array):
                    print(i,j,x)
                    if i + j + x == k and p1 != p2 and p3 != p1 and p2 != p3:
                        return (i, j, x)
        return None

if __name__=="__main__":
    assert(Solution.main(None, [1,2,3,4], 5)) == None
    assert(Solution.main(None, [1,2,3,4], 6)) == (1,2,3)
    assert(Solution.main(None, [4,3,2,1], 6)) == (3,2,1)
    assert(Solution.main(None, [5,5,3,1], 9)) == (5,3,1)
    assert(Solution.main(None, [5,5,3,1], 13)) == (5,5,3)
    assert(Solution.main(None, [5,5,3,1,2,3,4,5,6,7], 13)) == (5,5,3)
