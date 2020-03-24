# Given an array of numbers and a number k, determine 
# if there are three entries in the array which 
# add up to the specified number k. For example,
#  given [20, 303, 3, 4, 25] and k = 49, return 
# true as 20 + 4 + 25 = 49.


# class Solution:
#     def isK(self, arr, k):
#         sum = 0
#         for i in arr:
#             for j in arr:
#                 for z in arr:
#                     if i == j or j == z or i == z:
#                         pass
#                     else:
#                         sum = i + j + z
#                     if sum == k:
#                         return [i,j,z]
#         return

# print(Solution.isK(None, [1,2,3,4], 9))


# Given a set of points (x, y)
#  on a 2D cartesian plane, 
# find the two closest points.
#  For example, given the points
#  [(1, 1), (-1, -1), (3, 4), (6, 1), (-1, -6), (-4, -3)],
#  return [(-1, -1), (1, 1)].


# sqrt((x2-x1)^2+(y2-y1)^2) (x1,y1) (x2,y2)

class Solution:
    def closestPoints(self, listOfCoordinates):
        xList = []
        yList = []
        for coordinate in listOfCoordinates:
            xList.append(coordinate[0])
            yList.append(coordinate[1])
        minDist = 10000
        dist = 100000
        for x2 in xList:
            for x1 in xList:
                for y2 in yList:
                    for y1 in yList:
                        # print(x1,y1,x2,y2)
                        if x1 == x2 or y1 == y2:
                            pass
                        else:
                            dist = abs(((x2-x1)^2+(y2-y1)^2)^(1//2))
                        # print(dist)
                        if dist <= minDist:
                            minDist = dist
        print(minDist)
        return False

Solution.closestPoints(None,[(1,1),(2,2),(3,3)])

# for var in range(len(T)):
#   print (var,T[var])