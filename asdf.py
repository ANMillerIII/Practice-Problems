# # # Good morning! Here's your coding interview problem for today.

# # # This problem was asked by PagerDuty.

# # # Given a positive integer N, find the smallest number of steps it will take to reach 1.

# # # There are two kinds of permitted steps:

# # # You may decrement N to N - 1.
# # # If a * b = N, you may decrement N to the larger of a and b.
# # # For example, given 100, you can reach 1 in five steps with the following route: 100 -> 10 -> 9 -> 3 -> 2 -> 1.

# # # def main(N):
# # #     min = N
# # #     steps = 0
# # #     while N != 1:
# # #         for a in range(1,N//2+1):
# # #             for b in range(1,N//2+1):
# # #                 if N == a*b and (a <= min or b <= min):
# # #                     if a <= b:
# # #                         min = b
# # #                     else:
# # #                         min = a
# # #                 N = min
# # #         if N != 1:
# # #             N = N-1
# # #                     # print(a,b)
# # #         # print(min)
# # #                     # return 0
# # #         steps += 1
# # #         print(N)
# # #     return steps

# # # print(main(100)) # 5



# # # move1 = {"timestamp": 1526580382, count: 2, "type": "exit"}



# # #
# # # import datetime


# # def main():
# #     move1 = {"timestamp": 1526580382, "count": 5, "type": "enter"}
# #     move2 = {"timestamp": 1526580390, "count": 3, "type": "enter"}
# #     move3 = {"timestamp": 1526580440, "count": 8, "type": "exit"}
# #     move4 = {"timestamp": 1526580450, "count": 1, "type": "enter"}
# #     move5 = {"timestamp": 1526580461, "count": 1, "type": "exit"}
# #     moves = [move1,move2,move3, move4, move5]
# #     peopleInBuilding = 0
# #     max = 0
# #     busiestTime =  0
# #     for index, move in enumerate(moves):
# #         if move["type"] == "enter":
# #             peopleInBuilding += move["count"]
# #             if peopleInBuilding > max:
# #                 max = peopleInBuilding
# #                 busiestTime =  int(moves[index+1]["timestamp"]) - int(move["timestamp"])
# #                 a = int(moves[index+1]["timestamp"])
# #                 b = int(move["timestamp"])
# #         else:
# #             peopleInBuilding -= move["count"]
    
# #         # print(peopleInBuilding)
# #     return a, b, busiestTime
        




# #     # print(datetime.time())
# #     # dict1 = {"a": 1, "b": 2, "c": [1,2,3,"as",True], 1: "fifteen"}
# #     # list1 = ["a",["asdf"],{1:1}]
# #     # print(list1[2][1])
# #     # for i,j in dict1.items():
# #     #     print(i)
# #     #     print(j)
# # print(main())



# Given a positive integer N, find the smallest number of steps it will take to reach 1.

# There are two kinds of permitted steps:

# You may decrement N to N - 1.
# If a * b = N, you may decrement N to the larger of a and b.
# For example, given 100, you can reach 1 in five steps with the following route: 100 -> 10 -> 9 -> 3 -> 2 -> 1.










# class data:
#     val = 0
#     steps = 0

# def minStepToReachOne(N):
#     queue = data()
#     while !q.empty():
#         if t.val == 1:
#             return t.steps


# #include <bits/stdc++.h> 
# using namespace std; 
  
# //  structure represent one node in queue 
# struct data 
# { 
#     int val; 
#     int steps; 
#     data(int val, int steps) : val(val), steps(steps) 
#     {} 
# }; 
  
# //  method returns minimum step to reach one 
# int minStepToReachOne(int N) 
# { 
#     queue<data> q; 
#     q.push(data(N, 0)); 
  
#     // set is used to visit numbers so that they 
#     // won't be pushed in queue again 
#     set<int> st; 
  
#     //  loop untill we reach to 1 
#     while (!q.empty()) 
#     { 
#         data t = q.front();     q.pop(); 
          
#         // if current data value is 1, return its 
#         // steps from N 
#         if (t.val == 1) 
#             return t.steps; 
  
#         //  check curr - 1, only if it not visited yet 
#         if (st.find(t.val - 1) == st.end()) 
#         { 
#             q.push(data(t.val - 1, t.steps + 1)); 
#             st.insert(t.val - 1); 
#         } 
  
#         //  loop from 2 to sqrt(value) for its divisors 
#         for (int i = 2; i*i <= t.val; i++) 
#         { 
  
#             // check divisor, only if it is not visited yet 
#             // if i is divisor of val, then val / i will 
#             // be its bigger divisor 
#             if (t.val % i == 0 && st.find(t.val / i) == st.end()) 
#             { 
#                 q.push(data(t.val / i, t.steps + 1)); 
#                 st.insert(t.val / i); 
#             } 
#         } 
#     }  
# } 
  
# //  Driver code to test above methods 
# int main() 
# { 
#     int N = 17; 
#     cout << minStepToReachOne(N) << endl;  
# } 
# d.update((k, v * 0.5) for k,v in d.items())

def pie_chart(data):
    total = 0
    new = {}
    for value in data.values():
        total += value
    for key,value in data.items():
        new[key] = round(value/total,1)*360
    return new
print(pie_chart({ "a": 8, "b": 21, "c": 12, "d": 5, "e": 4 }))