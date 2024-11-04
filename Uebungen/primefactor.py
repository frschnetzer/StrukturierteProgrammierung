def calculatePrimefactor(number, divider):
    results = []
    while number > 1:
        rest = number % divider
        if rest > 0: # no primenumber
            divider += 1
        else:
            results.append(divider)
            number = number // divider
    return results

print(calculatePrimefactor(51, 2))