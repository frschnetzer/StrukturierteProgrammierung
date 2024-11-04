def invert_number(number):
    reversedNumber = 0
    
    while number >= 1: # iterating throught number as long as number is bigger 1
        digit = number % 10 # get one digit from number (reading from other direction)
        reversedNumber = reversedNumber * 10 # get new position
        reversedNumber += digit # adding number to current position
        number //= 10 # moving to next digit in number

    return reversedNumber + 1

print(invert_number(454654))