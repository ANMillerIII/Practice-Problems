# # # from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E

# # # class Calculator:

# # #     def __init__(self, master):
# # #         self.master = master
# # #         master.title("Calculator")

# # #         self.total = 0
# # #         self.entered_number = 0

# # #         self.total_label_text = IntVar()
# # #         self.total_label_text.set(self.total)
# # #         self.total_label = Label(master, textvariable=self.total_label_text)

# # #         self.label = Label(master, text="Total:")

# # #         vcmd = master.register(self.validate) # we have to wrap the command
# # #         self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))

# # #         self.add_button = Button(master, text="+", command=lambda: self.update("add"))
# # #         self.subtract_button = Button(master, text="-", command=lambda: self.update("subtract"))
# # #         self.reset_button = Button(master, text="Reset", command=lambda: self.update("reset"))

# # #         # LAYOUT

# # #         self.label.grid(row=0, column=0, sticky=W)
# # #         self.total_label.grid(row=0, column=1, columnspan=2, sticky=E)

# # #         self.entry.grid(row=1, column=0, columnspan=3, sticky=W+E)

# # #         self.add_button.grid(row=2, column=0)
# # #         self.subtract_button.grid(row=2, column=1)
# # #         self.reset_button.grid(row=2, column=2, sticky=W+E)

# # #     def validate(self, new_text):
# # #         if not new_text: # the field is being cleared
# # #             self.entered_number = 0
# # #             return True

# # #         try:
# # #             self.entered_number = int(new_text)
# # #             return True
# # #         except ValueError:
# # #             return False

# # #     def update(self, method):
# # #         if method == "add":
# # #             self.total += self.entered_number
# # #         elif method == "subtract":
# # #             self.total -= self.entered_number
# # #         else: # reset
# # #             self.total = 0

# # #         self.total_label_text.set(self.total)
# # #         self.entry.delete(0, END)

# # # root = Tk()
# # # my_gui = Calculator(root)
# # # root.mainloop()
# # # -------------------------------------------------------------------------------------
# # # # Python code to demonstrate working of unittest 
# # # import unittest 
  
# # # class TestStringMethods(unittest.TestCase): 
      
# # #     def setUp(self): 
# # #         pass
# # #         # self.
# # #     # Returns True if the string contains 4 a. 
# # #     def test_strings_a(self): 
# # #         self.assertEqual( 'a'*4, 'aaaaa') 
  
# # #     # Returns True if the string is in upper case. 
# # #     def test_upper(self):         
# # #         self.assertEqual('foo'.upper(), 'FOO') 
  
# # #     # Returns TRUE if the string is in uppercase 
# # #     # else returns False. 
# # #     def test_isupper(self):         
# # # #         self.assertTrue('FOO'.isupper()) 
# # # #         self.assertFalse('Foo'.isupper()) 
  
# # # #     # Returns true if the string is stripped and  
# # # #     # matches the given output. 
# # # #     def test_strip(self):         
# # # #         s = 'geeksforgeeks'
# # # #         self.assertEqual(s.strip('geek'), 'sforgeeks') 
  
# # # #     # Returns true if the string splits and matches 
# # # #     # the given output. 
# # # #     def test_split(self):         
# # # #         s = 'hello world'self.
# # # #         self.assertEqual(s.split(), ['hello', 'world']) 
# # # #         with self.assertRaises(TypeError): 
# # # #             s.split(2) 
  
# # # # if __name__ == '__main__': 
# # # #     unittest.main()


# # # # 4. Write a Python class to get all possible unique subsets from a set of distinct integers. - Go to the editor
# # # # Input : [4, 5, 6]
# # # # Output : [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]]

# # # class unSub:

# # #     def unn(array):
# # #         outArray = []
# # #         for index, element in enumerate(array):
# # #             for index2, element in enumerate(array):
# # #                 if element not in outArray:
# # #                     outArray.append(element)
# # #         print(outArray)

# # # class py_solution:

# # #     def sub_sets(self, sset):
# # #         return self.subsetsRecur([], sorted(sset))
    
# # #     def subsetsRecur(self, current, sset):
# # #         if sset:
# # #             return self.subsetsRecur(current, sset[1:]) + self.subsetsRecur(current + [sset[0]], sset[1:])
# # #         return [current]

# # # print(py_solution().sub_sets([4,5,6]))



# # # if __name__ == '__main__':
# # #     main()


# # # import requests
# # # def main():
# # #     r = requests.get('https://maps.mpr.com/maps_code/pages_fc/group-emp.php?sector=%25')
# # #     print(r.text)
# # # # main()

# # # if __name__ == '__main__':
# # #     main()



# # class Complex:
# #     def __init__(self, realpart, imagpart):
# #         self.r = realpart
# #         self.i = imagpart
# # x = Complex(3.0,-4.5)
# # print(x.r,x.i)


# # class ReallyComplex(Complex):
# #     d


# class Polygon:
#     def __init__(self, no_of_sides):
#         self.n = no_of_sides
#         self.sides = [0 for i in range(no_of_sides)]
#     def inputSides(self):
#         self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]
#     def dispSides(self):
#         for i in range(self.n):
#             print("Side",i+1,"is",self.sides[i])

# class Triangle(Polygon):
#     def __init__(self):
#         Polygon.__init__(self,3)
#     def findArea(self):
#         a, b, c = self.sides
#         # calculate the semi-perimeter
#         s = (a + b + c) / 2
#         area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
#         print('The area of the triangle is %0.2f' %area)

# tri = Triangle()
# print(isinstance(tri,Polygon),issubclass(Polygon,Triangle))
# # tri.dispSides()


class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
