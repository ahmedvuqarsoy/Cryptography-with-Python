#Hajiahmad Ahmadzada Ceaser Input
#ENCRYPTION - function

def encryption(message, value):
    #Making all the letters capital
    message = message.upper()

    #Our default key value
    key = value

    #Ciphered text
    cipher = ""

    for i in range(len(message)):
        #Checking that it's alphanumeric value or not
        if(not (message[i].isalnum())):
            cipher += message[i]

        #Work on  text
        else:
            val = ord(message[i]) + key
            if(val > 90):
                val -= 26
            cipher += chr(val)
    return cipher

#--------------------------------------------------

#DECRYPTION - function

def decryption(message, key):
    #Making all the letters capital
    message = message.upper()

    #Our default key value
    key = 3

    #Ciphered text
    cipher = ""

    for i in range(len(message)):
        #Checking that it's alphanumeric value or not
        if(not (message[i].isalnum())):
            cipher += message[i]

        #Work on  text
        else:
            val = ord(message[i]) - key
            if(val < 65):
                val += 26
            cipher += chr(val)
    return cipher


#--------------------------- MAIN PART ---------------------------#

print("""
______________Ceaser Cipher Encryption System______________\n
.............. Enter 1 for encryption:
.............. Enter 2 for decryption:
""")

#Input the private key
key = int(input("Please enter the private key: "))

#Input the string to decrypt or to encrypt
message = input("Please enter your message: ")

#Command for decryption or encryption
command = int(input("_______Your command: "))

#Work-flow
if(command == 1):
    print(encryption(message, key))
elif( command == 2):
    print(decryption(message, key))
else:
    print("ERROR! UNKNOWN COMMAND")
