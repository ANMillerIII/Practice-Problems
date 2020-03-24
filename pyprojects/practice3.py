# Excersise 23

# def main():

#     with open('primenumbers.txt', 'r') as fPrime:
#         with open('happynumbers.txt', 'r') as fHappy:
#             linesBoth = []
#             linesPrime = fPrime.readlines()
#             linesHappy = fHappy.readlines()
#             for line in linesPrime:
#                 if line in linesHappy:
#                     linesBoth.append(int(line.rstrip()))
#         return linesBoth
        
# Excersise 24



# def drawBoard():
#     size = int(input('Board size? '))
#     print(' ---'*size)
#     for i in range(1, size+1):
#         print('|   '*(size+1))
#         print(' ---'*size)


# drawBoard()


# Exercise 25

# import math
# numGuess = 0

# def main():
#     num = int(input('Number? '))
#     return num

# def guessNum(guess,num):
#     global numGuess
#     numGuess += 1
#     print(guess)
#     if guess == num:
#         return numGuess
#     elif num > guess:
#         return guessNum(int(math.ceil(guess + (100-guess)//2)),num)
#     else:
#         return guessNum(int(math.ceil(guess-guess//2)),num)

# print(guessNum(50,main()))

# create a dictionary of names and birthday
# ask user to enter name
# return birthay of that person back


# Excersise 33

# birthList = {
#     'Albert Einstein' : '01/17/1707',
#     'Al Miller' : '09/20/3000'
# }

# class Birthdays:

#     def lookUpBirthday(self):
#         name = str(input('Whose birthday do you want to look up?'))
#         try:
#             print(birthList[name])
#         except:
#             print('Name not in dictionary!')

#     def addBirthday(self):
#         name = str(input('Whose birthday do you want to add?'))
#         birthday = str(input('What\'s their birthday?'))
#         try:
#             with open('info.json', 'w') as f:
#                 json.dump(, f)
#             birthList[name] = birthday
#         except:
#             birthList

# Birthdays.lookUpBirthday(None)
# Birthdays.addBirthday(None)
# Birthdays.lookUpBirthday(None)



# Excersise 34

# import json

# class Birthdays:

#     with open('info.json', 'w+') as f:
#         a = f.write('{}')
#     with open('info.json', 'r') as f:
#         birthList = json.load(f)

#     def lookUpBirthday(self):
#         name = str(input('Whose birthday do you want to look up?'))
#         try:
#             print(birthList[name])
#         except:
#             print('Name not in dictionary!')

#     def addBirthday(self):
#         name = str(input('Whose birthday do you want to add?'))
#         birthday = str(input('What\'s their birthday?'))
#         a = {name: birthday}
#         with open('info.json', 'w') as f:
#             json.dump(a, f)
#             try:
#                 f[name] = birthday
#             except:
#                 pass
#             print(f)


# Birthdays.lookUpBirthday(None)
# Birthdays.addBirthday(None)
# Birthdays.lookUpBirthday(None)

# Excersise 35

# import requests
# from bs4 import BeautifulSoup

# # print full text

# def tagVis(element):
#     if element.parent.name in ['style', 'script', 'head', 'title', 'meta']:
#         return False
#     if isinstance(element, Comment):
#         return False
#     return True

# def main():
#     site = requests.get('http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture')
#     soupy = BeautifulSoup(site.text, 'html.parser')
#     texts = soupy.findAll(text=True)
#     print(texts)
#     # visTexts = filter(tag_soupy.findAll(text=True)
#     # for line in BeautifulSoup.find_all(class_='story-heading')
# main()


# from bs4 import BeautifulSoup
# from bs4.element import Comment
# import urllib.request


# def tag_visible(element):
#     if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
#         return False
#     if isinstance(element, Comment):
#         return False
#     return True


# def text_from_html(body):
#     soup = BeautifulSoup(body, 'html.parser')
#     texts = soup.findAll(text=True)
#     visible_texts = filter(tag_visible, texts)  
#     return u" ".join(t.strip() for t in visible_texts)

# html = urllib.request.urlopen('http://www.nytimes.com/2009/12/21/us/21storm.html').read()
# print(text_from_html(html))


# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# # import numpy



# # x = 

# apl_price = [12,414,32,333,32,111]
# ms_price = [32,121,44,5,666,7]
# year = [2012,2013,2014,2015,2016,2017]

# plt.title('ASDFASDF')
# plt.plot3D(year, apl_price)
# plt.plot(year, ms_price)
# plt.xlabel('Year')
# plt.ylabel('Stock')
# plt.show()

# # fig_1 = plt.figure(1, figsize=(6,6))
# # fig_2 = plt.figure(2, figsize=(6,6))
# # chart_1 = fig_1.add_subplot(121)
# # chart_2 = fig_2.add_subplot(121)


from matplotlib.ticker import NullFormatter  # useful for `logit` scale
import numpy as np
import matplotlib.pyplot as plt
# Fixing random state for reproducibility
np.random.seed(19680801)

# make up some data in the interval ]0, 1[
y = np.random.normal(loc=0.5, scale=0.4, size=1000)
y = y[(y > 0) & (y < 1)]
y.sort()
x = np.arange(len(y))

# plot with various axes scales
plt.figure()

# linear
plt.subplot(221)
plt.plot(x, y)
plt.yscale('linear')
plt.title('linear')
plt.grid(True)


# log
plt.subplot(222)
plt.plot(x, y)
plt.yscale('log')
plt.title('log')
plt.grid(True)


# symmetric log
plt.subplot(223)
plt.plot(x, y - y.mean())
plt.yscale('symlog', linthreshy=0.01)
plt.title('symlog')
plt.grid(True)

# logit
plt.subplot(224)
plt.plot(x, y)
plt.yscale('logit')
plt.title('logit')
plt.grid(True)
# Format the minor tick labels of the y-axis into empty strings with
# `NullFormatter`, to avoid cumbering the axis with too many labels.
plt.gca().yaxis.set_minor_formatter(NullFormatter())
# Adjust the subplot layout, because the logit one may take more space
# than usual, due to y-tick labels like "1 - 10^{-3}"
plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25,
                    wspace=0.35)

plt.show()