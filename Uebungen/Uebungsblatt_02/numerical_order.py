def numberical_order(n):
    divider = 3
    while n != 0:
        if(n % divider == 0):
            n += 4
        elif(n % (divider + 1) == 0):
            n //= 2
        else:
            n -= 1
print(numberical_order(4))