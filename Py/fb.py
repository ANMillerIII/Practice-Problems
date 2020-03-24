# how many ways can 0-9 map etc. go? 

def num_ways(data):
    nums = [str(i - 96) for i in range(97,123)]
    alphas = [chr(i) for i in range(97,123)]
    count = 0
    for char in data:
        for num in nums:
            if char == num:
                data.remove(char)
            
        if char =
    return count
    # for num in nums:
    #     if num is in data:
    #         data.remove(nums)
    #         count += 1
        
print(num_ways("12345"))