# def progress_days(runs):
# 	progress = 0
# 	for index,run in enumerate(runs):
# 		if index != 0 and run > runs[index-1]:
# 			progress += 1
# 	return progress

# print(progress_days([3,4,1,2]))

# def get_length(lst):
#     count = 0
#     while len
#         r
#         if type(element) == int:
#             count += 1
#         else:
#             for el2 in element:
#                 count += 1
#     return count

# print(get_length([1,2,[4,5]])) # 4

# def remainder(x, y):
#     while x-y >= 0:
#         x -= y
#     return x

# print(remainder(13,6))

# def edabit(str):
#     if not str:
#         return False
#     if "edabit" in str:
#         return True
#     return False
def edabit(txt):
    for c in txt:
        if "e" in txt:
            if "d" in txt[txt.index("e"):]:
                if "a" in txt[txt.index("d"):]:
                    if "b" in txt[txt.index("a"):]:
                        if "i" in txt[txt.index("b"):]:
                            if "t" in txt[txt.index("i"):]:
                                return "YES"
                            return "NO"
                        return "NO"
                    return "NO"
                return "NO"
            return "NO"
        return "NO"
    return "NO"
print(edabit("a"))