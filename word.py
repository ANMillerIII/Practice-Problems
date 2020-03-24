WORD_MAP = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}


def get_char_count_dict(string):
    letter_dict = dict()
    for char in string:
        if char not in letter_dict:
            letter_dict[char] = 0
        letter_dict[char] += 1
    return letter_dict


def use_digit(letter_dict, word_dict, digit):
    for char in word_dict:
        if char not in letter_dict or word_dict[char] > letter_dict[char]:
            return letter_dict, 0

    for char in word_dict:
        letter_dict[char] -= word_dict[char]

    letter_dict, uses = use_digit(letter_dict, word_dict, digit)
    return letter_dict, uses + 1


def get_sorted_nums(string):
    letter_dict = get_char_count_dict(string)

    result = 0
    for i in range(10):
        word = WORD_MAP[i]
        word_dict = get_char_count_dict(word)
        letter_dict, uses = use_digit(letter_dict, word_dict, i)

        while uses > 0:
            result = result * 10 + i
            uses -= 1

    return result


# Tests
assert get_sorted_nums("niesevehrtfeev") == 357
assert get_sorted_nums("nienienn") == 99
assert get_sorted_nums("enieniennon") == 199


































# # # for word in words
# # # while true
# #     # if every letter in word is in string
# #             # add word to sorted str
# #             # remove letters
# #             # add index to list
# #     # else
# #         # False
# # # sort list of indexes

# class Solution:
#     def sortAna(self, string):
#         sSet = set(string)
#         sList = list(string)
#         sortedStr = ''
#         indexes = []
#         words = ['zero','one','two','three','four','five','six','seven','eight','nine']
#         for word in words:
#             sSet = set(sList)
#             if set(word).issubset(sSet):
#                 indexes.append(words.index(word))
#                 for letter in sList:
#                     sList.remove(letter)
        
#                 # sSet.remove(word)
#         print(sSet)
#         print(sList)
#         print(indexes)
#         return

# Solution.sortAna(None, 'treefiveh')


# from collections import defaultdict

# def load_words(filename='/usr/share/dict/american-english'):
#     with open(filename) as f:
#         for word in f:
#             yield word.rstrip()

# def get_anagrams(source):
#     d = defaultdict(list)
#     for word in source:
#         key = "".join(sorted(word))
#         d[key].append(word)
#     return d

# def print_anagrams(word_source):
#     d = get_anagrams(word_source)
#     for key, anagrams in d.iteritems():
#         if len(anagrams) > 1:
#             print(key, anagrams)

# word_source = load_words()
# print_anagrams(word_source)





































# # print(set('aebc').issubset(set('abcd')))
# # # print(set('') <= set('ba') and set('') is not None)
# # # print(set
# # # def pangram():
# # # n = str(input('give me a word to check if it is a pangram:\n'))
# # # n = n.lower()
# # # n = n.replace(' ','')
# # # if not isinstance(n, str):
# # #     return n, False
# # # elif set(n) >= set('abcdefghijklmnopqrstuvxywz'):
# # #     return n, True
# # # else: 
# # #     return n, False
# # #         return 

# # # Solution.sortAna(None, 'trhee')

# # # import string

# # # alphabet = set(string.ascii_lowercase)

# # # def ispangram(input_string):
# # #     return set(input_string.lower()) >= alphabet

# # class Solution:
# #     def __init__(self):
# #         pass
# #     def sortAna(self, string):
# #         sList = list(string)
# #         sortedStr = ''
# #         indexs = []
# #         words = ['zero','one','two','three','four','five','six','seven','eight','nine']
# #         for word in words:
# #             while True:
# #                 for letter in word:
# #                     # print(word, letter, sList, sortedStr, indexs)
# #                     if letter in sList:
# #                         sList.remove(letter)
# #                         sortedStr += letter
# #                     else:
# #                         break
# #                 indexs.append(words.index(word))
# #                 break
# #             print(sList)
# #             print(sortedStr)
                