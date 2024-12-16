def toLower(text, pattern):
    text = text.lower()
    pattern = pattern.lower()
    return text, pattern

def toLower_02(text):
    newText = ""
    for char in text:
        if ord(char) >= 97 or ord(char) == 32:
            newText += char
        else:
            newText += chr(ord(char) + 32)
    return newText

def searchPattern(text, pattern, caseSensitive = True): # setting default values
    if caseSensitive == False: # make text and pattern to lower case to ignore case sensitivity
        #text, pattern = toLower(text, pattern)   
        text = toLower_02(text) 
        pattern = toLower_02(pattern)
    
    positions = []
    # we use range to get integers
    for pos in range(len(text) - len(pattern) + 1): #  iterate through text with calculated space of pattern length when at the end of text
        if text[pos:pos + len(pattern)] == pattern: # get block from text that is exact long as the pattern and check if its pattern
            positions.append(pos)
    return positions

def testSearchPattern():
    text= "Dieses da ist Es es Es"
    pattern = "Es"
    positions = searchPattern(text, pattern, caseSensitive=False)
    if positions == [14, 20]:
        return True
    return False

def main():
   print(testSearchPattern())
main()