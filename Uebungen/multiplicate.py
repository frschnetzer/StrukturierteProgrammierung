def multiplicate(end, multiplicator):
    a = 1
    while a <= end:
        result = a * multiplicator
        print(f"{a} * {multiplicator} = {result}")
        a += 1

print(multiplicate(5, 2))