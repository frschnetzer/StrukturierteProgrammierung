def main():
    def generate_word(letter, n):
        counter = 0
        word = ''
        while counter < n:
            word += letter
            counter += 1
        return word

    def replace_uneven(word, letter):
        word = list(word)
        counter = 0
        while counter < len(word):
            if counter % 2 != 0:
                word[counter] = letter
            counter += 1
        word = ''.join(word)
        return word
    
    def replace_A(word, symbol):
        counter = 0
        word = list(word)
        while counter < len(word):
            if counter % 2 == 0:
                word[counter] = symbol
            counter += 1
        word = ''.join(word)
        return word

    word = generate_word('A', 5)
    print(f"Word with replaced letter: {word}")
    replaced_word = replace_uneven(word, 'B')
    print(f"Word with replaced letter: {replaced_word}")
    replacedA = replace_A(replaced_word, '#')
    print(f"Word with replaced a: {replacedA}")

main()