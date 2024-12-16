def Reverse(char):
    if len(char) == 1: # if char is just one character we do not need to reverse it
        return char 
    else:
        return Reverse(char[1:]) + char[0] # get the second element of the input word till we reach the end. When we go up we put the chars together

def main():
    word = ""
    print(f"Test with empty string: Input: {word} -> Output: {Reverse(word)}")

    word = "a"
    print(f"Test with one character: Input: {word} -> Output: {Reverse(word)}")

    word = "abc"
    print(f"Test with word: Input: {word} -> Output: {Reverse(word)}")
main()