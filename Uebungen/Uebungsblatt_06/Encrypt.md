# Encrypt Algorithm

## Encrypt(IN text, OUT encryptedText)
seperators = [',', '.', ' ']  <!-- create list with valid seperators -->\
specialWords = {'heute': 'nretsO', 'Bahnhof': '402U', 'alle': 'hci'}\
encryptedText = emtpy string\
counter = 0\
for char in text  <!-- iterating through the whole input text -->\
    word = empty string  <!-- create empty string to store word -->\
    if char is not in separators\
		word = AppendCharToWord(IN char, OUT word)\
	else\
        if counter == 4\
            AppendWordToEncryptedText(IN word)\
            counter = 0\
        else if word is in specialWords\
            encryptedSpecialWord = FindAndReplaceWord(IN word, OUT encryptedSpecialWord)\
            AppendWordToEncryptedText(IN encryptedSpecialWord)\
        else\
            encryptedWord = EncryptWord(IN word, OUT encryptedWord)\
            AppendWordToEncryptedText(IN encryptedWord)\
            if encryptedSeperator is not empty string <!-- find duplicate seperators and ignore them -->\
                encryptedSeperator = EnryptSeperator(IN char, OUT encryptedSeperator)\
                AppendWordToEncryptedText(IN encryptedSeperator)\
                encryptedSeperator = empty string\
    counter +1\
return encryptedText\

## AppendCharToWord(IN char, OUT word)
    word += char\

## AppendWordToEncrytedText(IN word)
    encryptedText += word\

## FindAndReplaceWord(IN word, OUT encryptedSpecialWord)
    for key in specialWords\
        if word == key\
            return value\

## EncryptWord(IN word, OUT encryptedWord)
    encryptedWord = empty string\
    for char in word from last element to first\
        encryptedWord += char\
    return encryptedWord\

## EnryptSeperator(IN char, OUT encryptedSeperator)
    if char == ','\
        return '@'\
    else if char == '.'\
        return '#'\
    else:\
        return Random(['?','%','&'])\
