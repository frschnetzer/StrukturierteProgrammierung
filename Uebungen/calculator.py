# def GetOperand(entry):
#     #operand = entry[-2] # assumption that operand is always 2nd last char in entry
#     for i in entry: # iterating through entry till we find an operand
#         operandList = ['+', '-', '*', '/']
#         if i in operandList: # check if valid operation
#             return i

# def GetNumbers(entry): #get numbers by slicing
#     number = 0
#     numbers = []
#     isEnd = False
#     for i in entry:
#         if i != " ":
#             digit = ord(i) - ord('0')
#             number = (number * 10) + digit
#         else:
#             numbers.append(number)
#             number = 0



#     while not isEnd:
#         for i in entry:

#     return numbers

# def calculator(entry):
#     operand = GetOperand(entry)
#     numbers = GetNumbers(entry)
    
#     # like a switch case statement for all valid operations
#     operations = {
#         '+': lambda x, y: x + y,
#         '-': lambda x, y: x - y,
#         '*': lambda x, y: x * y,
#         '/': lambda x, y: x / y
#     }

#     result = operations[operand](numbers[0], numbers[1])
#     return result

# def main():
#     #entry = input()
#     entry = "10  200000 + "
#     print(calculator(entry))
#     entry = "1 2 - "
#     print(calculator(entry))
#     entry = "1 2 * "
#     print(calculator(entry))
#     entry = "1 2 / "
#     print(calculator(entry))
# main()





