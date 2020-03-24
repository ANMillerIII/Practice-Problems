import matplotlib.pyplot as plt
import csv

# make class that is CASE - has test int, maint int, unreliability, PHP, P_LP, P_OPS
class Case:
    def __init__(self,Num,TI,MI,VU):
        self.Num = Num
        self.MI = MI
        self.TI = TI
        self.VU = VU

    def calcProbs(self,VU):
        self.P_HP = (1-(1-self.VU)**4)**2
        self.P_LP = 1-(1-self.VU**2)**6
        self.P_OPS = 1-(1-self.P_LP)*(1-self.P_HP)
        return self.P_OPS

# instead, read CSV
with open('probs.csv','r') as b:
    Cases = csv.reader(b)


print(Cases[0][0])
# Cases = []
# for index, TI in enumerate(TestInts):
#     Cases.append(Case(index+1,TestInts[index],MaintInts[index],valveUnreliabilities[index]))

# for case in Cases:
#     case.P1 = (case.calcProbs(case.VU)/Cases[0].P_OPS)*2.00E-6

# overallProbs = [case.P1 for case in Cases]
# caseNums = [case.Num for case in Cases]
# plt.bar(caseNums,overallProbs)
# plt.title('Missile Generation Probability')
# plt.xlabel('Case')
# plt.ylabel('P1')
# plt.show()



# Cases = []
# for index, TI in enumerate(TestInts):
#     Cases.append(Case(index+1,TestInts[index],MaintInts[index],valveUnreliabilities[index]))

# for case in Cases:
#     case.P1 = (case.calcProbs(case.VU)/Cases[0].P_OPS)*2.00E-6

# overallProbs = [case.P1 for case in Cases]
# caseNums = [case.Num for case in Cases]
# for prob in overallProbs:
#     print(prob)
# plt.bar(caseNums,overallProbs)
# plt.title('Missile Generation Probability')
# plt.xlabel('Case')
# plt.ylabel('P1')
# plt.show()


















# TestInts = [3, 6, 9, 18, 3, 6, 9, 18]
# MaintInts = [108, 108, 108, 108, 126, 126, 126, 126]
# valveUnreliabilities = [3.68E-04, 7.32E-04, 1.09E-03, 2.14E-03, 4.10E-04, 8.14E-04, 1.21E-03, 2.39E-03]














# # 
# import matplotlib.pyplot as plt
# import random

# # xValues = [0,1,2,3,4,10]
# # yValues = [10,11,12,13,14,15]

# # plt.plot(xValues, yValues)

# # plt.show()


# # x = [random.randint(1,100) for x in range(0,10)]
# # y = [random.randint(1,100) for y in range(0,10)]

# # plt.plot(x,y)
# # plt.show()


# import matplotlib.pyplot as plt 

# x_vals = list(range(11)) 
# squares = [x**2 for x in x_vals] 
# cubes = [x**3 for x in x_vals] 
# fig, axarr = plt.subplots(1, 2, sharex=True) 
# axarr[0].scatter(x_vals, squares) 
# axarr[0].set_title('Squares') 
# axarr[1].scatter(x_vals, cubes, c='cyan') 
# axarr[1].set_title('Cubes') 
# plt.show()

# calculate P1 based on given unreliability sets
# how to copy and jsonify from text?
# # P_HP

# (1-(1-D2)**4)**2

# # P_LP
# 1-(1-D3**2)**6

# # P_OPS
# 1-(1-E2)*(1-F2)