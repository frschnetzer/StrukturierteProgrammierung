number = 51
divider = 2

while number > 1:
    rest = number % divider
    if rest > 0: # no primenumber
        divider += 1

    else:
        print(divider)
        number = number // divider

def function_with_multiple_returns():
    a = 10
    return a, 100, "hello"

a = function_with_multiple_returns()
print(a)