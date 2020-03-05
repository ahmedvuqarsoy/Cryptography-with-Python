import math

#Plaintext: Common sense is not so common.
#Ciphertext: Cenoonommstmme oo snnio. s s c
#Key: 8


def encryption(plaintext, key):
    #Creating strings in the count of key
    ls = [""]*key

    #Traverse on given string and each char
    #Goes to different string
    i = 0
    col = 0
    while(i < len(plaintext)):
        ls[(col) % key] += plaintext[i]
        i += 1
        col += 1

    #Connect all the strings
    ciphertext = ""
    for i in ls:
        ciphertext += i

    return ciphertext

def decryption(message, key):
    numOfColumns = int(math.ceil(len(message) / float(key)))
    numOfRows = key
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)
    plaintext = [''] * numOfColumns
    #If encryption 8 column 4 row (decryption 4 column 8 row)
    column = 0
    row = 0

    for symbol in message:
        plaintext[column] += symbol
        column += 1

        if (column == numOfColumns) or (column == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
            column = 0
            row += 1

    return ''.join(plaintext)


def main():

    command = int(input("""
    _____Columnar Transposition Cipher_____
    === CLICK
    = 1. For Encryption =
    = 2. For Decryption =
    
    Your Command: 
    """))

    key = int(input("Please, enter your key: "))
    text = input("Please, enter the string: ")

    if( key < 2 or key > len(text)//2):
        print("Key is unvalid.")
        exit(1)

    if(command == 1):
        print(encryption(text, key))
    elif(command == 2):
        print(decryption(text, key))
    else:
        print("Unvalid command.")
        exit(1)

if __name__ == "__main__":
    main()
