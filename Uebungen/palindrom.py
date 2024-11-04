# umkehren der input zahl
def generate_inverse(input):
    inverse = 0
    while input > 0:
        digit = input % 10
        inverse *= 10
        inverse += digit
        input //= 10
    return inverse

# überprüfen, ob input mit generirtem inverse ein palindrom ergibt
def is_palindrom(input_number):
    comparer = generate_inverse(input_number)
    if comparer == input_number:
        return True
    else:
        return False

print(f"Is input a palindrom: {is_palindrom(1234321)}")