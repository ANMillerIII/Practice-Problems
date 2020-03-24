import sys

def main():
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        sys.exit("usage: py prime num")
    max = int(sys.argv[1])
    primes = []
    with open("output.txt", "w") as f:
        for num in range(1,max+1):
            temp = 0
            for x in range(1, num):
                if num % x == 0 and x != 1:
                    temp += 1
            if temp == 0:
                primes.append(num)
        print(primes, file=f)


if __name__== "__main__":
    main()
    
    