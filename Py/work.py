# # class Person:
# #     def __init__(self, person_name, person_age):
# #         self.name = person_name
# #         self.age = person_age

# # class Student(Person):
# #     def __init__(self, student_name, student_age):
# #         Person.__init__(self, student_name, student_age)



# # # Create an object of the superclass
# # person1 = Person("Richard", 23)

# # # Create an object of the subclass
# # student1 = Student("Max", 22)

# # print(vars(student1))
# # print(vars(person1))

# # def parenth(str):
# #     for i,char in enumerate(str):
# #         if char == '(':
# #             char2 = ''
# #             j = 1
# #             while not char2 == ')' and len(str) > 0:
# #                 char2 = str[len(str)-j]
# #                 j += 1
# #             else:
# #                 s = ''
# #                 str = str[:(len(str)-j)] + s + str[(len(str)-j) + 1:]
# #                 str = str[:i] + s + str[i + 1:]
# #     print(str)
# #     if not '(' in str:
# #         return "valid"
# #     print(str)
# #     return "invalid"

# # print(parenth('(())('))















# # def parenth(str):
# #     positions = []
# #     for i,char in enumerate(str):
# #         if char == '(':
# #             for j,char in enumerate(str[(i):]):
# #                 print(str[i:])
# #                 if char == ')' and not j in positions:
# #                     positions.append(j)
# #                 elif char =='(':
# #                     positions = []
# #                 # elif char == '(':
# #                 #     pass
# #     print(len(positions), positions, int(len(str)/2))
# #     if len(positions) == int(len(str)/2):
# #         return "valid"
# #     return "invalid"



# # print(parenth('('))
# # print(parenth('()'))
# # print(parenth('())'))

# # print(parenth('()()'))






# def check(myStr):
#     open_list = ['('] 
#     close_list = [')'] 
#     stack = [] 
#     for i in myStr: 
#         if i in open_list: 
#             stack.append(i) 
#         elif i in close_list: 
#             pos = close_list.index(i) 
#             if ((len(stack) > 0) and
#                 (open_list[pos] == stack[len(stack)-1])): 
#                 stack.pop() 
#             else: 
#                 return "Unbalanced"
#     if len(stack) == 0: 
#         return "Balanced"
  
# # Driver code 
# string = "()"
# print(string,"-", check(string)) 
  
# # string = "[{}{})(]"
# # print(string,"-", check(string)) 