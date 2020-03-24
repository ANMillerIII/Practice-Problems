# def harshad(n):
#     clusterLength = 0
#     if n > 100:
#         num = n-100
#     else:
#         num = 1
#     while True:
#         string = str(num)
#         sumDigits = 0
#         for digit in string:
#             sumDigits += int(digit)
#         if num % sumDigits == 0:
#             if num == n:
#                 clusterLength += 1
#                 position = clusterLength
#                 clusterLength2 = clusterLength
#                 num2 = num
#                 while True:
#                     string2 = str(num2)
#                     sumDigit2 = 0
#                     for digit2 in string2:
#                         sumDigit2 += int(digit2)
#                     if num2 % sumDigit2 != 0:
#                         return [clusterLength2-1, position]
#                     else:
#                         clusterLength2 += 1
#                         num2 += 1
#             else:
#                 clusterLength += 1
#         elif num == n and num % sumDigits != 0:
#             return [0, 0]
#         else:
#             clusterLength = 0
#         num += 1


# print(harshad(10810245632))


def num_to_eng(n):
    # alphas = {"one":1,"two":2,"three":3,"four": 4,"five": 5,"six": 6,"seven": 7,"eight":8,"nine":9,"ten":10}
    alphas = {0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten"}
    string = str(n)
    words = ""
    for digit in string:
        words += alphas[int(digit)] + " "
    return words
print(num_to_eng(500))

fifty
forty
one hunder
two hundred
one thousand