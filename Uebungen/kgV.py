def ggT(a,b):
    while b != 0:
        a, b = b, a % b # divide till 0 remainder and swaping numbers based on euklid
    return a

# kleinste gemeinsame Vielfache
def calculate_kgV(a, b):
    return(a * b) // ggT(a, b)

print(f"Calculated kgV: {calculate_kgV(6,8)}")
