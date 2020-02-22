#Cracking Caesar Cipher using Bruteforce by Hajiahmad Ahmadzada

import time

def bruteforce(encrypted_message):

    encrypted_message.upper()
    #There is 26 letter and we check each combination
    #in normal Caesar Cipher
    for key in range(1,27):
        decrypted_message = ""

        #We decrypt message between keys 1 and 26
        for i in range(len(encrypted_message)):
            if(not(encrypted_message[i].isalnum())):
                decrypted_message += encrypted_message[i]
            else:
                value = ord(encrypted_message[i]) - key

                if(value < 65):
                    value += 26
                decrypted_message += chr(value)

        print("The used key = ",key)
        print("The possible decrypted message: ", decrypted_message)
        time.sleep(2)

        #We ask to user is it possible decryption or not.
        print("------------------------")
        ans = input("Continue? Y/N: ")
        print("------------------------")
        if(ans == "Y" or ans == "y"):
            continue
        else:
            break




encrypted_message = input("""
----------------------------------
Please enter your encrypted string
----------------------------------

=> """)
    
bruteforce(encrypted_message)
