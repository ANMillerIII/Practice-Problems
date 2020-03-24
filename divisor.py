# Divide without divisor symbol, in O(log(n)) time.
# 12-31-19

def divide(n, div):
    rem = 1
    mult = 0
    if div >= n:
        return "Divisor must be less than number."
    while rem > 0:
        rem = n - div
        n -= div
        mult += 1
        if rem - div <= 0:
            return (mult, rem)

if __name__ == "__main__":
	print(divide(1,2))