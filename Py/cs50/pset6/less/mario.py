# get correct input for height 1-8
while True:
    height = input("Height? ")
    if height.isdigit() and int(height) >= 1 and int(height) <= 8:
        break
height = int(height)

# make pyramid
for i in range(1, height + 1):
    print(" "*(height - i) + "#"*i)
