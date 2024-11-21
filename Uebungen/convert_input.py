def convert_input(input):
    number = 0
    for i in input:
        result = ord(i) - ord('0')
        number = (number *10) + result
    return number

print(convert_input("123"))