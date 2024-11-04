def dec_to_bin(d):
    if d == 0:
        print(0)
    while int(d) > 0:
        print(d % 2)
        d //= 2

print("Please enter a number")
d = int(input())

dec_to_bin(d)