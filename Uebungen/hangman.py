import random
def  main():
    def generate_word(word, replacement):
        counter = 0
        replacedWord = ""
        while counter < len(word):
            replacedWord += replacement
            counter += 1
        return replacedWord
    
    def replace_char(word, char, position):
        word = list(word)
        word[position] = char
        return ''.join(word)

    def hangman():
        tries = 10
        isFound = False
        examples = ['python', 'hangman', 'test']
        randomWord = random.choice(examples)
        placeholder = generate_word(randomWord, '_')
        usedChars = []
        while tries > 0:            
            print(f"The word: {placeholder}")
            print(f"Used chars: {usedChars}")
            entry = input()
            position = 0
            for i in randomWord:
                if entry == i:
                    print("Found a char!")
                    isFound = True
                    placeholder = replace_char(placeholder, i, position)

                position += 1
                   
            if isFound == False:
                print("Entry is not in word")
                usedChars.append(entry)
                tries -=1
            isFound = False
        print("You are out of tries!")
        
    print(hangman())
main()