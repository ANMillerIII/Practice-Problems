def maxSub(arr):
    repeats = []
    max = count = 0
    for element in arr:
        if element in repeats:
            if count > max:
                max = count
            count = 0
            repeats = []
        else:
            repeats.append(element)
            count += 1
    return max

print(maxSub([1,2,1,4,5,1,2,3]))