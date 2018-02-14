#Text file encryption project
from string import ascii_lowercase as aLower
import itertools

print('Welcome to the Encryptor v1.0\n\n')
print('This program encrypts text files with a user defined key.')
print('Please note that your message will always come out as lowercase.')
print('Please avoid texts where capitalization is important.')

while True:
    defaultList = []
    extras = ['.',',','-','!','?','#','@','(',')','*','/','%',' ', '\"', '\"','/','\\',':',';']
    for x in aLower:
        defaultList.append(x)
    for x in range(10):
        defaultList.append(str(x))
    for x in extras:
        defaultList.append(x)



    inputString =  str(input("\n\nPlease enter your text: ")).lower()
    while True:
    #This loop checks the user key to see if it fits the criteria.
        try:
            encryptKey = int(input("\nPlease enter the encryption key (4 digits from 0-9): "))
        except ValueError:
            print ("\nPlease enter a number using digits.")
            continue
        if len(str(encryptKey)) != 4:
            print("\nPlease enter 4 digits")
            continue
        else:
            encryptKey = str(encryptKey)
            break
    
    def textHandler(text): #Handles the text input by reversing it and splitting it up
        textReverse = text[::-1]
        textLetters = []
        for x in textReverse:
            textLetters.append(x)
        return textLetters


    def keyHandler(key): #Handles the key into values
        keyList = []
        keySum = 0 

        for x in key: #Adds each digit to the key list
            keyList.append(int(x))

        for x in keyList: #Sums the digits
            keySum += x

        return keyList

    def encrypt0r(textList,keyList,letterList): #Encrypting the string using the key
        encryptedList = []
        encryptedStr = ""
        letterMap = {letter: i for i, letter in enumerate(letterList)}

        for character, key in zip(textList, itertools.cycle(keyList)):
            if character in letterMap:
                tempIndex = letterMap[character] + key # This ups the index value of each 
                encryptedList.append(letterList[tempIndex%len(letterList)]) #  letter by a digit of the keyList
            else:
                encryptedList.append(character) 
        encryptedStr = "".join(encryptedList)
        return encryptedStr

    print('\n\nEncrypted!\n\n' + encrypt0r(textHandler(inputString),keyHandler(encryptKey),defaultList))