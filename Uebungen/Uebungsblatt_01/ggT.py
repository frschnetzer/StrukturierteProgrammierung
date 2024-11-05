def primefactor(number):
    primenumber = 2
    factors = []
    while primenumber * primenumber <= number:
        while (number % primenumber) == 0:
            factors.append(primenumber)
            number //= primenumber
        primenumber += 1
    if number > 1:
        factors.append(number)
    return factors

def kgV(a,b):
    primNumbersA = primefactor(a)
    primNumbersB = primefactor(b)
    
    kgv = 1
    for factor in primNumbersA:
        if factor in primNumbersB:
            primNumbersB.remove(factor)
        kgv*= factor
            
    for factor in primNumbersB:
        kgv*= factor
    
    return kgv
    
def kgV_02(a,b):
    primNumbersA = primefactor(a)
    primNumbersB = primefactor(b)
    factors = [] 

    for factor in primNumbersA:
        if factor in primNumbersB:
            primNumbersB.remove(factor)
        factors.append(factor)
            
    for factor in primNumbersB:
        factors.append(factor)
    
    kgv = 0
    for i in factors:
        kgv *= i
    return kgv

print(kgV(60,70))