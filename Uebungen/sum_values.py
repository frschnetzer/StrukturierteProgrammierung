def splitNumber(number):
    return list(map(int,str(number)))

def splitNumbersLong(number):
    digit = 0
    splittedNumbers = []
    while number > 0:
        digit = number % 10
        splittedNumbers.append(digit)
        number //= 10
    splittedNumbers
    return splittedNumbers

print(splitNumber(321))
splittedNumbers = splitNumbersLong(321)

def sum_values(values):
    sum = 0
    for digit in values:
        sum += digit
    return sum

print(sum_values(splittedNumbers))